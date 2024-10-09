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

    # Sync the unpaid subscription with the session cart
    if unpaid_subscription_info:
        subscription_id = str(unpaid_subscription_info.subscription.id)

        if not session_cart:
            session_cart[subscription_id] = {
                'subscription_type': unpaid_subscription_info.subscription.subscription_type,
                'auto_renew': unpaid_subscription_info.auto_renew,
            }
            request.session['cart'] = session_cart
        else:
            attach_subscription_to_profile(user, session_cart)

    request.session.modified = True  # Ensure the session is marked as modified


@receiver(post_save, sender=User_Subscriptions)
def update_profile_on_subscription_change(sender, instance, **kwargs):
    """
    Handle updating the user's subscription info if the subscription changes
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
    Ensures only one unpaid subscription is stored.
    """
    print("Signal 'handle_user_logout' triggered")

    session_cart = request.session.get('cart', {})
    print(f"Session cart: {session_cart}")  # Print the contents of the session cart

    if session_cart:
        try:
            user_profile = user.user_profile
            print(f"User profile found: {user_profile}")
        except User_Profile.DoesNotExist:
            print(f"No profile found for user: {user.username}")
            return  # If no profile exists, nothing to do

        # Delete any existing unpaid subscription before saving the new one
        Subscription_Info_For_User.objects.filter(user_profile=user_profile, paid=False).delete()

        # Attach the new subscription from the session cart to the user's profile
        for item_id in session_cart.keys():
            try:
                subscription = User_Subscriptions.objects.get(pk=item_id)
                print(f"Subscription found: {subscription}")
                # Create the new Subscription_Info_For_User
                Subscription_Info_For_User.objects.create(
                    user_profile=user_profile,
                    subscription=subscription,
                    paid=False,  # Mark as unpaid until actual payment is made
                    auto_renew=session_cart[item_id].get('auto_renew', False),
                )
                print(f"New unpaid subscription saved to profile: {subscription}")
            except User_Subscriptions.DoesNotExist:
                print(f"Subscription with ID {item_id} does not exist")
                continue

        # Clear the cart from the session
        request.session['cart'] = {}
        request.session.modified = True  # Ensure the session is marked as modified
        print("Session cart cleared and modified")