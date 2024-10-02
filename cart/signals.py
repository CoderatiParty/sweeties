from django.contrib.auth.signals import user_logged_in
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from subscriptions.models import User_Subscriptions


@receiver(user_logged_in)
def restore_cart_on_login(request, user, **kwargs):
    """
    Restore the user's unpaid subscription from the database into the session cart.
    Ensure only one unpaid subscription exists.
    """
    profile = user.user_profile  # Get the user's profile

    # Fetch the unpaid subscription linked to this user's profile
    unpaid_subscription = User_Subscriptions.objects.filter(
        user_profile=profile,  # Correct reference to the user profile
        paid=False  # Only unpaid items, i.e., items in the cart
    ).first()

    # If there's an unpaid subscription, recreate the session cart with this item
    if unpaid_subscription:
        request.session['cart'] = {
            str(unpaid_subscription.id): {
                'type': unpaid_subscription.type,
                'description': unpaid_subscription.description,
                'cost': str(unpaid_subscription.cost),  # Convert Decimal to string for session storage
                'duration_years': unpaid_subscription.duration_years,
                'duration_days': unpaid_subscription.duration_days,
                'auto_renew': unpaid_subscription.auto_renew,
                'image': unpaid_subscription.image.url if unpaid_subscription.image else None,
            }
        }
        request.session.modified = True  # Ensure session changes are saved
    else:
        # If no unpaid subscription, make sure the cart is empty
        request.session['cart'] = {}


@receiver(user_signed_up)
def link_unpaid_subscriptions_on_signup(request, user, **kwargs):
    """
    Link the session's unpaid subscription to the user's profile after successful signup.
    Ensure only one unpaid subscription exists.
    """
    profile = user.user_profile

    # Remove any existing unpaid subscriptions for this user (ensuring only one subscription in the cart)
    User_Subscriptions.objects.filter(subscription__user=profile.user, paid=False).delete()

    # Check if there is an item in the session cart
    if 'cart' in request.session and len(request.session['cart']) == 1:
        item_id, item_data = next(iter(request.session['cart'].items()))  # Get the first item (since there's only one)

        # Create a new subscription for the cart
        subscription = User_Subscriptions.objects.create(
            type=item_data['type'],
            description=item_data['description'],
            cost=item_data['cost'],
            duration_years=item_data.get('duration_years', 1),
            duration_days=item_data.get('duration_days', None),
            auto_renew=item_data['auto_renew'],
            image=item_data['image'],
            paid=False  # Mark as unpaid to indicate it's in the cart
        )

        # Associate this subscription with the user's profile (if necessary)
        profile.subscription = subscription
        profile.save()