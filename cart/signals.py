import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from subscriptions.models import User_Subscriptions


logger = logging.getLogger(__name__)


@receiver(user_signed_up)
def save_session_cart_to_profile(sender, request, user, **kwargs):
    """
    When a user signs up, save the session cart to the user's profile.
    """
    cart = request.session.get('cart', {})
    logger.debug(f"Session cart contents during signup: {cart}")

    if cart:
        profile = user.user_profile  # Get the user's profile

        # Clear any existing subscription in the profile
        profile.subscription = None  # Clear previous subscription
        
        for item_id in cart.keys():
            try:
                subscription = User_Subscriptions.objects.get(pk=item_id)

                # Assign the new subscription to the user's profile
                profile.subscription = subscription
                profile.save()

                logger.info(f"Assigned subscription {subscription} to user profile for {user.username}.")
            except User_Subscriptions.DoesNotExist:
                logger.error(f"Subscription with id {item_id} does not exist.")
                continue
    else:
        logger.info(f"No items in cart during signup for user {user.username}.")


@receiver(user_logged_in)
def manage_cart_and_profile_on_login(sender, request, user, **kwargs):
    """
    Manage the user's cart and profile based on login scenarios:
    - Scenario 1: User logs in with a subscription in the cart.
    - Scenario 2: User logs in with nothing in the cart.
    """
    profile = user.user_profile  # Get the user's profile
    cart = request.session.get('cart', {})
    logger.debug(f"Session cart contents during login: {cart}")

    # Scenario 1: User logs in with a subscription in the cart
    if cart:
        item_id = next(iter(cart.keys()))  # Get the first item ID from the cart
        try:
            subscription = User_Subscriptions.objects.get(pk=item_id)

            # Check if the stored subscription in the profile is unpaid
            if profile.subscription and not profile.subscription.paid:
                # Update the profile's subscription to the new one from the cart
                profile.subscription = subscription
                profile.save()
                logger.info(f"Updated user profile with new subscription {subscription} for user {user.username}.")

                # Re-add the updated subscription to the cart
                request.session['cart'] = {
                    subscription.id: {
                        'type': subscription.type,
                        'description': subscription.description,
                        'cost': str(subscription.cost),  # Convert Decimal to string for JSON serialization
                        'duration_years': str(subscription.duration_years),  # Convert to string
                        'auto_renew': subscription.auto_renew,
                        'image': subscription.image.url if subscription.image else None,
                    }
                }
                request.session.modified = True  # Mark the session as modified
                logger.info(f"Re-added subscription {subscription} to the cart for user {user.username}.")
            elif profile.subscription and profile.subscription.paid:
                # User already has a paid subscription
                logger.warning(f"User {user.username} already has a paid subscription. Emptying cart.")
                request.session['cart'] = {}  # Empty the cart
                request.session.modified = True  # Mark the session as modified
                # Optionally, you could set a message to inform the user
            else:
                logger.info(f"No unpaid subscription found for user {user.username}.")

        except User_Subscriptions.DoesNotExist:
            logger.error(f"Subscription with id {item_id} does not exist in the cart.")
            # Handle cases where the subscription might not exist

    # Scenario 2: User logs in with nothing in the cart
    else:
        if profile.subscription and not profile.subscription.paid:
            # Re-add the stored unpaid subscription to the cart
            subscription = profile.subscription
            request.session['cart'] = {
                subscription.id: {
                    'type': subscription.type,
                    'description': subscription.description,
                    'cost': str(subscription.cost),  # Convert Decimal to string for JSON serialization
                    'duration_years': str(subscription.duration_years),  # Convert to string
                    'auto_renew': subscription.auto_renew,
                    'image': subscription.image.url if subscription.image else None,
                }
            }
            request.session.modified = True  # Mark the session as modified
            logger.info(f"Re-added stored subscription {subscription} to the cart for user {user.username}.")
        else:
            logger.info(f"No unpaid subscriptions found in profile for user {user.username}. The cart remains empty.")

@receiver(user_logged_out)
def update_profile_on_logout(sender, request, user, **kwargs):
    """
    Update the user's profile with the current cart subscription on logout.
    Scenario 3: A logged-in user changes their subscription in the cart then logs out.
    """
    profile = user.user_profile  # Get the user's profile
    cart = request.session.get('cart', {})

    if cart:
        item_id = next(iter(cart.keys()))  # Get the first item ID from the cart
        try:
            subscription = User_Subscriptions.objects.get(pk=item_id)

            # Update profile subscription if the subscription is unpaid
            if profile.subscription and not profile.subscription.paid:
                # Store the new subscription from the cart in the profile
                profile.subscription = subscription
                profile.save()
                logger.info(f"User {user.username} logged out. Updated profile with new subscription {subscription}.")
            else:
                logger.info(f"User {user.username} logged out. No updates to the profile since paid subscription exists.")
                
        except User_Subscriptions.DoesNotExist:
            logger.error(f"Subscription with id {item_id} does not exist in the cart.")
    else:
        logger.info(f"User {user.username} logged out with an empty cart. No updates to the profile.")