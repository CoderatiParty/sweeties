from django.shortcuts import render, get_object_or_404
from .models import User_Subscriptions
from decimal import Decimal
from django.conf import settings

# Create your views here.

def subscriptions(request):
    """ A view to show subscriptions page """

    # Get all categories to display in the menu
    subscriptions = User_Subscriptions.objects.all()
    vat_multiplier = Decimal(settings.VAT_MULTIPLIER)

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

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


def subscription(request, subscription_id):
    """ A view to show each article in full """

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    subscriptions = User_Subscriptions.objects.all()

    subscription = get_object_or_404(User_Subscriptions, pk=subscription_id)

    context = {
        'subscriptions': subscriptions,
        'subscription': subscription,
        'current_path': current_path,
        'referrer': referrer,
    }

    return render(request, 'subscriptions/subscription.html', context)