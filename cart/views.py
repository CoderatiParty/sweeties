from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.urls import reverse
from profiles.models import User_Profile


# Create your views here.

def view_cart(request):
    """
    A view to show the cart page
    """
    cart = request.session.get('cart', {})
    subscription = None
    user_has_paid_subscription = False

    # Check if the user is authenticated
    if request.user.is_authenticated:
        user_profile = get_object_or_404(User_Profile, user=request.user)
        subscription_infos = Subscription_Info_For_User.objects.filter(user_profile=user_profile)
        # Check if the user has any paid subscriptions
        if subscription_infos.filter(paid=True).exists():
            user_has_paid_subscription = True

    for item_id, item_data in cart.items():
        subscription = get_object_or_404(User_Subscriptions, pk=item_id)

    return render(request, 'cart/view_cart.html', {'cart': cart, 'subscription': subscription, 'user_has_paid_subscription': user_has_paid_subscription})


def add_to_cart(request, item_id):
    """
    Adds a subscription to the cart.
    """
    if request.method == 'POST':
        # Fetch the subscription item from the database
        subscription = get_object_or_404(User_Subscriptions, pk=item_id)
        redirect_url = request.POST.get('redirect_url', '/')
        cart = request.session.get('cart', {})

        # Get auto_renew from the form (if applicable)
        auto_renew = request.POST.get('auto_renew', False)

        if request.user.is_authenticated:
            user_profile = get_object_or_404(User_Profile, user=request.user)
            # Check if there are unpaid subscriptions
            unpaid_subscription = Subscription_Info_For_User.objects.filter(paid=False).first()

            if unpaid_subscription:
                unpaid_subscription.delete()

            Subscription_Info_For_User.objects.create(
                user_profile=user_profile,
                subscription=subscription,
                paid=False,  # Since it's unpaid, set this to False
                auto_renew=auto_renew
            )

            cart.clear()

            cart[subscription.id] = {
                'subscription_type': subscription.subscription_type,
                'cost': str(subscription.cost),
                'duration_years': str(subscription.duration_years),
                'auto_renew': auto_renew,
            }
            request.session['cart'] = cart  # Save the updated cart in the session

            # Success message with a link to view the cart
            cart_url = reverse('view_cart')
            message = mark_safe(f'Subscription added to the cart successfully! <a href="{cart_url}">View Cart</a>')
            messages.success(request, message)
        else:
            cart.clear()
            # Handle the case for anonymous users, store cart info in the session
            cart[subscription.id] = {
                'subscription_type': subscription.subscription_type,
                'cost': str(subscription.cost),
                'duration_years': str(subscription.duration_years),
                'auto_renew': auto_renew,
            }
            request.session['cart'] = cart  # Save the updated cart in the session

            # Success message with a link to view the cart
            cart_url = reverse('view_cart')
            message = mark_safe(f'Subscription added to the cart successfully! <a href="{cart_url}">View Cart</a>')
            messages.success(request, message)
            
        # Redirect to the provided URL
        return redirect(redirect_url)

    # If the request method is not POST, redirect to a fallback page
    return redirect('/')


def update_auto_renew(request, item_id):
    """
    Updates the auto renew setting for the user.
    """
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        item_id_str = str(item_id)

        if item_id_str in cart:
            auto_renew = request.POST.get('auto_renew') == '1'
            cart[item_id_str]['auto_renew'] = auto_renew

            request.session['cart'] = cart
            if auto_renew:
                messages.success(request, "Auto-renew has been enabled for this subscription.")
            else:
                messages.success(request, "Auto-renew has been disabled for this subscription.")
        else:
            messages.error(request, "This item is not in your cart.")

        return redirect('view_cart')

    return redirect('view_cart')


def remove_from_cart(request, item_id):
    """
    Removes the subscription from the cart
    """
    request.session['cart'] = {}  # Clear the cart
    messages.success(request, 'Subscription removed from cart.')
    return redirect('view_cart')