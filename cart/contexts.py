from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from subscriptions.models import User_Subscriptions


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        def isinstance(item_data, int):
            subscription = get_object_or_404(User_Subscriptions, pk=item_id)
            total += item_data * subscription.cost
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'subscription': subscription,
            })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
