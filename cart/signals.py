from django.contrib.auth.signals import user_logged_in
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from subscriptions.models import User_Subscriptions


@receiver(user_logged_in)
def transfer_cart_to_user(sender, user, request, **kwargs):
    cart = request.session.get('cart', {})

    for subscription_id, quantity in cart.items():
        subscription = get_object_or_404(User_Subscriptions, id=subscription_id)
        
        # Here you would save the cart items to the user profile, such as:
        # CartItem.objects.create(user=user, product=product, quantity=quantity)
        # You would need to implement the CartItem model if you haven't yet

    # Clear the session cart after transfer
    request.session['cart'] = {}


@receiver(user_signed_up)
def transfer_cart_after_signup(request, user, **kwargs):
    # Similar logic to transfer cart items from session to user profile
    cart = request.session.get('cart', {})

    for subscription_id, quantity in cart.items():
        product = get_object_or_404(User_Subscriptions, id=subscription_id)
        
        # Save the cart items to the user profile
        # CartItem.objects.create(user=user, product=product, quantity=quantity)

    # Clear the session cart after transfer
    request.session['cart'] = {}