from django.shortcuts import render
from .models import User_Subscriptions

# Create your views here.

def cart(request):
    """ A view to show subscriptions page """

    # Get all categories to display in the menu
    subscriptions = User_Subscriptions.objects.all()

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    context = {
        'subscriptions': subscriptions,
        'current_path': current_path,
        'referrer': referrer,
    }

    return render(request, 'cart/cart.html', context)