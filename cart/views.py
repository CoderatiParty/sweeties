from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from .models import User_Subscriptions
from django.contrib import messages

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
        if cart:
            messages.error(request, 'You already have a subscription in your cart. Please remove it before adding a new one.')
        else:
            # Add the subscription to the cart. Only one item allowed.
            cart[subscription.id] = {
                'type': subscription.type,
                'cost': str(subscription.cost),  # Convert Decimal to string for session storage
                'duration_years': str(subscription.duration_years),
                'auto_renew': subscription.auto_renew,
                'image': subscription.image.url if subscription.image else None
            }

            messages.success(request, f'{subscription.type} Subscription added to cart!')

        # Save the cart back into the session
        request.session['cart'] = cart

        # Redirect to the provided redirect URL
        return redirect(redirect_url)

    # If the request method is not POST, redirect to a fallback page
    return redirect('/')


def remove_from_cart(request):
    """ Remove the subscription from the cart """
    request.session['cart'] = {}  # Clear the cart
    messages.success(request, 'Subscription removed from cart.')
    return redirect('cart')  # Replace 'cart' with the appropriate view or URL name
