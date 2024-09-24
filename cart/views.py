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
    """ Add the subscription to the cart """

    subscription = get_object_or_404(User_Subscriptions, pk=item_id)
    quantity = int(1)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    messages.success(request, f'Added {subscription.description} to the cart')

    request.session['cart'] = cart
    return redirect(redirect_url)
