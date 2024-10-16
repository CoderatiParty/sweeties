from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from .models import Order, OrderLineItem
from django.contrib.auth.decorators import login_required
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User
from profiles.models import User_Profile
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents
from datetime import timedelta
import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Function to cache checkout data
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):
    """
    View for checkout page
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})

    subscription = None

    for item_id, item_data in cart.items():
        subscription = get_object_or_404(User_Subscriptions, pk=item_id)

    # Get the profile for the authenticated user
    profile, created = User_Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        # Prefill auto-renew data for each subscription in the cart
        current_cart = cart_contents(request)

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }

        profile_form = UserProfileForm(form_data, instance=profile)
        if profile_form.is_valid():

            # Save the profile form
            profile_form.save()

            # Calculate the total and grand total
            current_cart = cart_contents(request)
            grand_total = current_cart['grand_total']


            # Creates the order and links it to the user's profile
            order = Order.objects.create(
                user_profile=profile,
                stripe_pid=request.POST.get('client_secret').split('_secret')[0],
                original_cart=json.dumps(cart),
                grand_total=grand_total,
            )

            # Iterates over the cart items to create OrderLineItems
            for item_id, item_data in cart.items():
                try:
                    subscription = User_Subscriptions.objects.get(id=item_id)
                    # Extracts the auto_renew status from the session cart
                    auto_renew = item_data.get('auto_renew', False)
                    quantity = 1
                    # Creating OrderLineItem for the subscription
                    order_line_item = OrderLineItem(
                        order=order,
                        subscription=subscription,
                        quantity=quantity
                    )
                    order_line_item.save()

                    # Calculates the renew date based on the subscription's duration_days
                    duration_days = subscription.duration_days
                    if duration_days == 365:
                        renew_date = order.date + timedelta(days=366)
                    elif duration_days == 1461:
                        renew_date = order.date + timedelta(days=1462)
                    else:
                        renew_date = None  # Handle other cases if needed

                    # Checks if an unpaid subscription already exists for this user
                    unpaid_subscription_info = Subscription_Info_For_User.objects.filter(
                        user_profile=profile,
                        subscription=subscription,
                        paid=False
                    ).first()

                    if unpaid_subscription_info:
                        # Update the unpaid subscription to mark it as paid
                        unpaid_subscription_info.paid = True
                        unpaid_subscription_info.payment = order  # Link to the new order
                        unpaid_subscription_info.auto_renew = auto_renew
                        unpaid_subscription_info.renew_date = renew_date
                        unpaid_subscription_info.save()
                    else:
                        # Create the subscription info as paid if no unpaid subscription exists
                        subscription_info = Subscription_Info_For_User.objects.create(
                            user_profile=profile,
                            subscription=subscription,
                            payment=order,  # Link to the order for payment info
                            auto_renew=auto_renew,
                            renew_date=renew_date,
                            paid=True  # Set this to true since payment has been processed
                        )
                        subscription_info.save()

                except User_Subscriptions.DoesNotExist as e:
                    messages.error(request, (
                        "One of the subscriptions in your cart wasn't "
                        "found in our database. "
                        "Please call us for assistance!"
                    ))
                    order.delete()
                    return redirect(reverse('view_cart'))

            # Saves the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST

            # Redirects to the checkout success page, passing the order number
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double-check your information.'))
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse('subscriptions'))

        # Stripe payment setup
        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Prefills the form with the user's profile information
        if request.user.is_authenticated:
            profile = User_Profile.objects.get(user=request.user)
            profile_form = UserProfileForm(initial={
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'email': profile.email,
                'phone_number': profile.phone_number,
            })

    if not stripe_public_key:
        messages.warning(request, ('Stripe public key is missing. '
                                   'Did you forget to set it in '
                                   'your environment?'))

    template = 'checkout/checkout.html'
    context = {
        'profile_form': profile_form,
        'subscription': subscription,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Displays page for successful checkouts
    """

    user_has_paid_subscription = False
    auto_renew_status = None

    # Check if the user is authenticated
    if request.user.is_authenticated:
        user_profile = get_object_or_404(User_Profile, user=request.user)
        subscription_infos = Subscription_Info_For_User.objects.filter(user_profile=user_profile)

        # Check if the user has any paid subscriptions
        if subscription_infos.filter(paid=True).exists():
            user_has_paid_subscription = True

        # Check if the user has selected auto_renew
        if subscription_infos.filter(auto_renew=True).exists():
            auto_renew_status = True

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # Gets the related subscriptions for the order
    order_line_items = OrderLineItem.objects.filter(order=order)
    subscriptions = [item.subscription for item in order_line_items]

    if request.user.is_authenticated:
        profile = order.user_profile  # Accesses the related User_Profile
        if profile:
            email = profile.email  # Gets the email from the profile
        else:
            email = request.user.email  # Fallback to user email if profile is missing

        # Updates the profile with the save_info flag
        if save_info:
            profile_data = {
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'phone_number': profile.phone_number,
                'email': profile.email,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'profile': profile,
        'subscriptions': subscriptions,
        'order_line_items': order_line_items,
        'user_has_paid_subscription': user_has_paid_subscription,
        'auto_renew_status': auto_renew_status,
    }

    return render(request, template, context)