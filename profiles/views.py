from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User_Profile
from .forms import UserProfileForm
from django.contrib.auth.models import User
from checkout.models import Order
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User
from checkout.models import Order, OrderLineItem
from django.urls import reverse
from django.contrib.auth import logout


@login_required
def profile(request):
    """ A view to show profile page """

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

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    profile = get_object_or_404(User_Profile, user=request.user)

    if request.method == 'POST':
        # Bind the form to POST data
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            # Save the form data to the profile
            form.save()
            user = request.user
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()  # Save the User model with updated information
            messages.success(request, 'Your profile has been updated successfully!')

            return redirect('profile')  # Redirect to some 'profile' view after successful update
    else:
        # Prepopulate the form with the existing data
        form = UserProfileForm(instance=profile)
    
    orders = profile.orders.all()

    for order in orders:
        # Assuming there's only one subscription info per order, we fetch the first match
        subscription_info = Subscription_Info_For_User.objects.filter(
            user_profile=user_profile,
            payment=order  # Link to the correct order/payment
        ).first()

        # Add the renew_date as an attribute of the order object
        order.renew_date = subscription_info.renew_date if subscription_info else None

    template = 'profiles/profile.html'

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
        'auto_renew_status': auto_renew_status,
    }

    return render(request, template, context)


@login_required
def subscription_history(request, order_number):
    """
    A route to link to the checkout success view to display old orders 
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

    order = get_object_or_404(Order, order_number=order_number)
    order_line_items = OrderLineItem.objects.filter(order=order)
    subscriptions = [item.subscription for item in order_line_items]
    user = order.user_profile.user  # Access the user through the user_profile relationship
    profile = get_object_or_404(User_Profile, user=request.user)
    first_name = user.first_name
    last_name = user.last_name

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'from_profile': True,
        'order': order,
        'profile': profile,
        'subscriptions': subscriptions,
        'order_line_items': order_line_items,
        'first_name': first_name,
        'last_name': last_name,
        'user_has_paid_subscription': user_has_paid_subscription,
        'auto_renew_status': auto_renew_status,
    }

    return render(request, template, context)


@login_required
def delete_confirmation(request):
    """ A view to show the delete confirmation page """

    user_has_paid_subscription = False

    # Check if the user is authenticated
    if request.user.is_authenticated:
        user_profile = get_object_or_404(User_Profile, user=request.user)
        subscription_infos = Subscription_Info_For_User.objects.filter(user_profile=user_profile)
        # Check if the user has any paid subscriptions
        if subscription_infos.filter(paid=True).exists():
            user_has_paid_subscription = True

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    context = {
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'profiles/delete_confirmation.html', context)


@login_required
def delete_profile(request, user_id):
    """
    A page to delete the user profile.
    """
    user = User.objects.get(id=user_id)
    if request.method == 'POST' and user == request.user:
        request.session.flush()  # Clears all session data
        logout(request)
        user.delete()  # Delete the user and related profile
        messages.success(request, "Your profile has been deleted.")
        return redirect('home')  # Redirect to home or login page after deletion
    return redirect('home')  # Redirect back to profile if not POST