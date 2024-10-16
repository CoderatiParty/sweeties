from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User
from profiles.models import User_Profile
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.utils.safestring import mark_safe


def attach_subscription_to_profile(user, session_cart):
    """
    Attaches the subscription from the session cart to the user's profile.
    Ensures only one unpaid subscription is attached to the profile.
    """
    try:
        user_profile = user.user_profile
    except User_Profile.DoesNotExist:
        return  # If no profile exists, return early

    # User doesn't have a paid subscription, check the session cart
    cart = session_cart.get('cart', {})
    if cart:
        # Delete any existing unpaid subscription for this user
        Subscription_Info_For_User.objects.filter(user_profile=user_profile, paid=False).delete()

        # Attach the new subscription
        for item_id, item_data in cart.items():
            subscription = get_object_or_404(User_Subscriptions, pk=item_id)

            # Create the Subscription_Info_For_User for the user
            Subscription_Info_For_User.objects.create(
                user_profile=user_profile,
                subscription=subscription,
                auto_renew=item_data.get('auto_renew', False),
                paid=False,  # Mark as unpaid until actual payment is made
                renew_date=None  # Set this later based on payment confirmation
            )

    return 'subscription_attached'


@receiver(user_logged_in)
def handle_user_login(sender, request, user, **kwargs):
    """
    Handles user login by ensuring that only one unpaid subscription is stored.
    Replaces any previously stored unpaid subscription if the subscription in the cart has a different ID.
    If the cart is empty, attach the unpaid subscription to the session cart.
    """
    session_cart = request.session.get('cart', {})

    try:
        user_profile = user.user_profile
    except User_Profile.DoesNotExist:
        return  # If no profile exists, nothing to do

    # Check if the user has a paid subscription
    paid_subscription_info = Subscription_Info_For_User.objects.filter(
        user_profile=user_profile,
        paid=True
    ).first()

    if paid_subscription_info:
        # If the user has a paid subscription, clear the cart, show a message instead
        request.session['cart'] = {}
        profile_url = reverse('profile')
        message = mark_safe(f'You already have a paid subscription! <a href="{profile_url}">View Profile</a>')
        messages.success(request, message)
        return  # Don't proceed further if there's a paid subscription

    # Check if the user has an unpaid subscription
    unpaid_subscription_info = Subscription_Info_For_User.objects.filter(
        user_profile=user_profile,
        paid=False
    ).first()

    if unpaid_subscription_info:
        # If the cart is empty, add the unpaid subscription to the session cart
        if not session_cart:
            session_cart[str(unpaid_subscription_info.subscription.id)] = {
                'subscription_type': unpaid_subscription_info.subscription.subscription_type,
                'auto_renew': unpaid_subscription_info.auto_renew,
            }
            request.session['cart'] = session_cart
        else:
            # If the cart has a different subscription, replace the unpaid one
            for subscription_id, item_data in session_cart.items():
                cart_subscription = get_object_or_404(User_Subscriptions, pk=subscription_id)

                if unpaid_subscription_info.subscription.id != cart_subscription.id:
                    # Delete the existing unpaid subscription since it's a different one
                    unpaid_subscription_info.delete()

                # Sync the cart with the new or updated subscription (only one will remain)
                request.session['cart'] = {
                    subscription_id: {
                        'subscription_type': cart_subscription.subscription_type,
                        'auto_renew': item_data.get('auto_renew', False),
                    }
                }

                # If no unpaid subscription exists or it's replaced, add this one
                Subscription_Info_For_User.objects.create(
                    user_profile=user_profile,
                    subscription=cart_subscription,
                    auto_renew=item_data.get('auto_renew', False),
                    paid=False,  # Mark as unpaid
                    renew_date=None
                )

                # Break the loop after processing the first subscription in the cart
                break

    request.session.modified = True  # Mark the session as modified


@receiver(post_save, sender=User_Subscriptions)
def update_profile_on_subscription_change(sender, instance, **kwargs):
    """
    Handles updating the user's subscription info if the subscription changes
    and the user does not already have a paid subscription.
    """
    subscription_infos = Subscription_Info_For_User.objects.filter(subscription=instance)

    for subscription_info in subscription_infos:
        if not subscription_info.paid:
            subscription_info.subscription = instance
            subscription_info.save()


@receiver(user_logged_out)
def handle_user_logout(sender, request, user, **kwargs):
    """
    Handle user logout by saving the current subscription in the session cart
    to the user's profile before they log out.
    Ensures only one unpaid subscription is stored unless they have a paid subscription.
    """

    session_cart = request.session.get('cart', {})

    # Initialize `user_profile` to None
    user_profile = None

    # Try to get the user profile if the user is authenticated
    if user.is_authenticated:
        try:
            user_profile = user.user_profile
        except User_Profile.DoesNotExist:
            return  # If no profile exists, exit the function

    # If no user profile was found, return early to prevent further errors
    if not user_profile:
        return

    # Fetch any paid subscription info after we have confirmed `user_profile` exists
    paid_subscription_info = Subscription_Info_For_User.objects.filter(
        user_profile=user_profile,
        paid=True
    ).first()

    # If there's a session cart and no paid subscription, proceed to save unpaid subscriptions
    if session_cart:
        # Delete any existing unpaid subscription before saving the new one
        Subscription_Info_For_User.objects.filter(user_profile=user_profile, paid=False).delete()

        # If a paid subscription exists, do nothing further
        if paid_subscription_info:
            return
        else:
            # Attach the new subscription from the session cart to the user's profile
            for item_id in session_cart.keys():
                try:
                    subscription = User_Subscriptions.objects.get(pk=item_id)
                    # Create the new Subscription_Info_For_User
                    Subscription_Info_For_User.objects.create(
                        user_profile=user_profile,
                        subscription=subscription,
                        paid=False,  # Mark as unpaid until actual payment is made
                        auto_renew=session_cart[item_id].get('auto_renew', False),
                    )
                except User_Subscriptions.DoesNotExist:
                    continue