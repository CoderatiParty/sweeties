from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User
from profiles.models import User_Profile
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings


def attach_subscription_to_profile(user, session_cart):
    """
    Attach the subscription from the session cart to the user's profile 
    by creating or updating a Subscription_Info_For_User entry.
    """
    try:
        # Get the user's profile
        user_profile = user.user_profile
    except User_Profile.DoesNotExist:
        return  # If no profile exists, return early

    # Check if the user has an existing subscription that is paid
    existing_subscription_info = Subscription_Info_For_User.objects.filter(
        user_profile=user_profile,
        paid=True
    ).first()

    if existing_subscription_info:
        # If they already have a paid subscription, redirect to the profile page
        return 'has_paid_subscription'

    # User doesn't have a paid subscription, check the session cart
    cart = session_cart.get('cart', {})
    if cart:
        for item_id, item_data in cart.items():
            subscription = get_object_or_404(User_Subscriptions, pk=item_id)

            # Create or update the Subscription_Info_For_User for the user
            subscription_info, created = Subscription_Info_For_User.objects.update_or_create(
                user_profile=user_profile,
                subscription=subscription,
                defaults={
                    'auto_renew': item_data.get('auto_renew', False),
                    'paid': False,  # Mark as unpaid until actual payment is made
                    'renew_date': None  # Set this later based on payment confirmation
                }
            )

    return 'subscription_attached'


@receiver(user_logged_in)
def handle_user_login(sender, request, user, **kwargs):
    """
    Handle user login by syncing the session cart with the user's profile.
    If the user has an unpaid subscription, put it in the session cart.
    """
    session_cart = request.session.get('cart', {})

    try:
        user_profile = user.user_profile
    except User_Profile.DoesNotExist:
        return  # If no profile exists, nothing to do

    # Check if the user has an unpaid subscription
    unpaid_subscription_info = Subscription_Info_For_User.objects.filter(
        user_profile=user_profile,
        paid=False
    ).first()

    if unpaid_subscription_info:
        subscription_id = str(unpaid_subscription_info.subscription.id)

        # Place the unpaid subscription in the session cart if not already present
        if subscription_id not in session_cart:
            session_cart[subscription_id] = {
                'subscription_type': unpaid_subscription_info.subscription.subscription_type,
                'auto_renew': unpaid_subscription_info.auto_renew,
            }
            request.session['cart'] = session_cart

    # Attach any subscription in the session cart to the user's profile
    if session_cart:
        result = attach_subscription_to_profile(user, session_cart)

        if result == 'has_paid_subscription':
            return redirect('profile_page')  # Redirect to profile if they have a paid subscription
        if result == 'subscription_attached':
            return redirect('checkout')  # Redirect to checkout if subscription was attached


# Signal to update profile if cart subscription changes during checkout
@receiver(post_save, sender=User_Subscriptions)
def update_profile_on_subscription_change(sender, instance, **kwargs):
    """
    Handle updating the user's subscription info if the subscription changes
    and the user does not already have a paid subscription.
    """
    # Find all users who have this subscription in their subscription info
    subscription_infos = Subscription_Info_For_User.objects.filter(subscription=instance)

    for subscription_info in subscription_infos:
        # If the subscription is unpaid (paid=False), allow the update
        if not subscription_info.paid:
            # Update the subscription instance in Subscription_Info_For_User
            subscription_info.subscription = instance
            subscription_info.save()


@receiver(user_logged_out)
def handle_user_logout(sender, request, user, **kwargs):
    """
    Handle user logout by saving the current subscription in the session cart
    to the user's profile before they log out.
    """
    session_cart = request.session.get('cart', {})

    if session_cart:
        try:
            user_profile = user.user_profile
        except User_Profile.DoesNotExist:
            return  # If no profile exists, nothing to do

        # Save the cart's subscription to the user's profile
        for item_id in session_cart.keys():
            try:
                subscription = User_Subscriptions.objects.get(pk=item_id)
                # Create or update Subscription_Info_For_User
                Subscription_Info_For_User.objects.update_or_create(
                    user_profile=user_profile,
                    subscription=subscription,
                    defaults={
                        'paid': False,  # Mark as unpaid until actual payment is made
                        'auto_renew': session_cart[item_id].get('auto_renew', False),
                    }
                )
            except User_Subscriptions.DoesNotExist:
                continue  # If subscription does not exist, skip it

        # Clear the cart from the session
        request.session['cart'] = {}