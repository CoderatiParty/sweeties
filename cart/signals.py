from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from subscriptions.models import User_Subscriptions
from profiles.models import User_Profile
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


# Helper function to handle cart subscription attachment logic
def attach_subscription_to_profile(user, session_cart):
    """
    Attach the subscription from the session cart to the user's profile 
    if the user doesn't already have a paid subscription.
    """
    try:
        # Get user profile
        user_profile = user.user_profile
    except User_Profile.DoesNotExist:
        # In case profile does not exist for the user, return early
        return

    # Check if the user has an existing subscription with 'paid=True'
    if user_profile.subscription and user_profile.subscription.paid:
        # If they already have a paid subscription, redirect them to the profile page
        return redirect('profile_page')  # Replace with your actual profile page URL or view

    # User doesn't have a paid subscription, check the session cart
    cart = session_cart.get('cart', {})
    if cart:
        # Retrieve the subscription details from the session cart
        for item_id, item_data in cart.items():
            subscription = User_Subscriptions.objects.get(pk=item_id)

            # Update user's profile subscription with cart details
            user_profile.subscription = subscription
            user_profile.subscription.paid = False  # Mark as unpaid until actual payment is made
            user_profile.save()

    # Return back to the checkout page
    return redirect('checkout')  # Replace with your actual checkout page URL or view


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile, _ = User_Profile.objects.get_or_create(user=instance)

        request = getattr(instance, 'request', None)
        if request:
            logger.debug(f"Request found for user: {request.user}, session_cart: {request.session.get('cart', {})}")
            
            session_cart = request.session.get('cart', {})
            if session_cart:
                attach_subscription_to_profile(instance, session_cart)
            else:
                logger.debug(f"No items in session cart for user: {request.user}")
        else:
            logger.debug("No request object found for the user.")


@receiver(user_logged_in)
def handle_user_login(sender, request, user, **kwargs):
    """
    Handle what happens when a user logs in, including updating the profile
    based on the cart contents, or redirecting to their profile page if they 
    already have a paid subscription.
    """
    # Get the session cart (if any)
    session_cart = request.session.get('cart', {})

    # Check if the user already has an unpaid subscription in their profile
    user_profile = user.user_profile
    if user_profile.subscription and not user_profile.subscription.paid:
        # Place the unpaid subscription ID into the session cart if not already there
        subscription_id = user_profile.subscription.id
        
        # Check if the cart is empty or doesn't already contain this subscription ID
        if str(subscription_id) not in session_cart:
            session_cart[str(subscription_id)] = {
                'subscription_type': user_profile.subscription.subscription_type,
                # You can choose to include other details if needed, but not cost
            }
            request.session['cart'] = session_cart  # Save the updated cart to the session

    # Attach subscription to profile based on the session cart
    if session_cart:
        result = attach_subscription_to_profile(user, session_cart)

        # If the user already has a paid subscription, redirect to profile
        if result == 'has_paid_subscription':
            return redirect('profile_page')  # Replace with your actual profile page URL or view

        # If the subscription was attached successfully, return to the checkout page
        if result == 'subscription_attached':
            return redirect('checkout')  # Replace with your actual checkout page URL or view


# Signal to update profile if cart subscription changes during checkout
@receiver(post_save, sender=User_Subscriptions)
def update_profile_on_subscription_change(sender, instance, **kwargs):
    """
    Handle updating the user's profile if they change their subscription in the cart
    and they don't already have a paid subscription.
    """
    # Get all users who have this subscription in their profile
    profiles = User_Profile.objects.filter(subscription=instance)

    for profile in profiles:
        # If the subscription is unpaid (paid=False), allow the update
        if not profile.subscription.paid:
            profile.subscription = instance
            profile.save()


@receiver(user_logged_out)
def handle_user_logout(sender, request, user, **kwargs):
    """
    Handle what happens when a user logs out, ensuring that the current 
    subscription in their cart is stored against their profile before logout.
    """
    # Get the session cart (if any)
    session_cart = request.session.get('cart', {})

    # If the cart is not empty, save the cart's subscription to the user's profile
    if session_cart:
        try:
            user_profile = user.user_profile
        except User_Profile.DoesNotExist:
            return  # If no profile exists, nothing to do

        # We expect the cart to have subscription IDs
        for item_id in session_cart.keys():
            try:
                subscription = User_Subscriptions.objects.get(pk=item_id)
                # Update the user's profile with the cart's subscription
                user_profile.subscription = subscription
                user_profile.subscription.paid = False  # Ensure the subscription is marked unpaid
                user_profile.save()
            except User_Subscriptions.DoesNotExist:
                continue  # Handle case where subscription ID doesn't exist
            
        # Clear the cart from the session once saved to profile
        request.session['cart'] = {}