from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from .models import User_Subscriptions
from django.contrib import messages
from django.utils.safestring import mark_safe

# Create your views here.

def view_cart(request):
    """ A view to show the cart """


    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a subscription to the cart. Only one item can be in the cart at a time. """
    if request.method == 'POST':
        # Fetch the subscription item from the database
        subscription = get_object_or_404(User_Subscriptions, pk=item_id)

        # Retrieve the redirect URL from the form (or set a fallback URL)
        redirect_url = request.POST.get('redirect_url', '/')

        # Retrieve the cart from the session (default to empty dict if not exists)
        cart = request.session.get('cart', {})

        # If the cart already contains an item, prevent adding another one
        if cart:  # Assuming this check is for an already existing subscription in the cart
            cart_url = reverse('cart')  # Generate the URL for the cart page
            # Construct the message with HTML and mark it as safe
            message = mark_safe(f'You already have a subscription in your <a href="{cart_url}">cart</a>. Please remove it before adding a new one.')
            messages.error(request, message)
        else:
            # Add the subscription to the cart. Only one item allowed.
            cart[subscription.id] = {
                'type': subscription.type,
                'cost': str(subscription.cost), # Convert Decimal to string for session storage
                'duration_years': str(subscription.duration_years),
                'auto_renew': subscription.auto_renew,
                'image': subscription.image.url if subscription.image else None
            }

            cart_url = reverse('cart')  # Generate the cart URL
            success_message = mark_safe(f'Subscription added to your cart successfully! <a href="{cart_url}">View Cart</a>')
            messages.success(request, success_message)

        # Save the cart back into the session
        request.session['cart'] = cart

        # Redirect to the provided redirect URL
        return redirect(redirect_url)

    # If the request method is not POST, redirect to a fallback page
    return redirect('/')


def remove_from_cart(request, item_id):
    """ Remove the subscription from the cart """
    request.session['cart'] = {}  # Clear the cart
    messages.success(request, 'Subscription removed from cart.')
    return redirect('cart')  # Replace 'cart' with the appropriate view or URL name
