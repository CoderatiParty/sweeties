from django.shortcuts import render, get_object_or_404
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User
from profiles.models import User_Profile
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.utils.safestring import mark_safe

# Create your views here.

def subscriptions(request):
    """ A view to show subscriptions page """

    # Get all categories to display in the menu
    subscriptions = User_Subscriptions.objects.all()
    vat_multiplier = Decimal(settings.VAT_MULTIPLIER)

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    cart = request.session.get('cart', {})

    # If the cart already contains an item, prevent adding another one
    if cart:  # Assuming this check is for an already existing subscription in the cart
        cart_url = reverse('view_cart')  # Generate the URL for the cart page
        # Construct the message with HTML and mark it as safe
        message = mark_safe(f'You already have a subscription in your <a href="{cart_url}">cart</a>. Please remove it before adding a new one.')
        messages.error(request, message)

    context = {
        'subscriptions': [
            {
                'subscription': sub,
                'vat_cost': sub.cost * vat_multiplier  # Calculate the cost inc. VAT
            }
            for sub in subscriptions
        ],
        'current_path': current_path,
        'referrer': referrer,
    }

    return render(request, 'subscriptions/subscriptions.html', context)


def add_subscription(request, subscription_id):
    """ A view to show each article in full """

    user_has_paid_subscription = False

    # Check if the user is authenticated
    if request.user.is_authenticated:
        user_profile = get_object_or_404(User_Profile, user=request.user)
        subscription_infos = Subscription_Info_For_User.objects.filter(user_profile=user_profile)
        # Check if the user has any paid subscriptions
        if subscription_infos.filter(paid=True).exists():
            user_has_paid_subscription = True

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    subscriptions = User_Subscriptions.objects.all()

    subscription = get_object_or_404(User_Subscriptions, pk=subscription_id)

    context = {
        'subscriptions': subscriptions,
        'subscription': subscription,
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'subscriptions/add_subscription.html', context)