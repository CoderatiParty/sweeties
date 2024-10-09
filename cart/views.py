from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.urls import reverse

# Create your views here.

def view_cart(request):
    """ A view to show the cart """
    cart = request.session.get('cart', {})


    return render(request, 'cart/view_cart.html', {'cart': cart})


def add_to_cart(request, item_id):
    if request.method == 'POST':
        subscription = get_object_or_404(User_Subscriptions, pk=item_id)
        redirect_url = request.POST.get('redirect_url', '/')
        cart = request.session.get('cart', {})

        if cart:
            cart_url = reverse('view_cart')
            message = mark_safe(f'You already have a subscription in your <a href="{cart_url}">cart</a>. Please remove it before adding a new one.')
            messages.error(request, message)
        else:
            auto_renew = request.POST.get('auto_renew', False)  # Get from form data
            cart[subscription.id] = {
                'subscription_type': subscription.subscription_type,
                'cost': str(subscription.cost),
                'duration_years': str(subscription.duration_years),
                'auto_renew': auto_renew,  # Store auto-renew temporarily in the cart session
            }

            request.session['cart'] = cart
            success_message = mark_safe(f'Subscription added to your cart successfully! <a href="{reverse("view_cart")}">View Cart</a>')
            messages.success(request, success_message)

        return redirect(redirect_url)

    return redirect('/')


def update_auto_renew(request, item_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        item_id_str = str(item_id)

        if item_id_str in cart:
            auto_renew = request.POST.get('auto_renew') == '1'
            cart[item_id_str]['auto_renew'] = auto_renew

            request.session['cart'] = cart
            if auto_renew:
                messages.success(request, "Auto-renew has been enabled for this subscription.")
            else:
                messages.success(request, "Auto-renew has been disabled for this subscription.")
        else:
            messages.error(request, "This item is not in your cart.")

        return redirect('view_cart')

    return redirect('view_cart')



def remove_from_cart(request, item_id):
    """ Remove the subscription from the cart """
    request.session['cart'] = {}  # Clear the cart
    messages.success(request, 'Subscription removed from cart.')
    return redirect('view_cart')  # Replace 'cart' with the appropriate view or URL name
