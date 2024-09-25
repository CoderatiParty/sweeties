from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from subscriptions.models import User_Subscriptions


def cart_contents(request):
    cart_items = []
    total = Decimal(0)  # Using Decimal for accurate financial calculations
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        # Fetch the subscription from the database
        subscription = get_object_or_404(User_Subscriptions, pk=item_id)
        
        # Since item_data is a dictionary, extract the relevant information
        cost = Decimal(item_data['cost'])
        total += cost  # Add the cost to the total
        product_count += 1  # Assuming only one item per cart as per your logic
        
        cart_items.append({
            'item_id': item_id,
            'subscription': subscription,  # Pass the actual subscription object
            'cost': cost,
            'auto_renew': item_data['auto_renew'],
            'image': item_data['image'],
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context