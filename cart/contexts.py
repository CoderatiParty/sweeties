from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from subscriptions.models import User_Subscriptions


def cart_contents(request):
    cart_items = []
    vat = Decimal(0)
    cost = Decimal(0)
    total_cost = Decimal(0)
    total = Decimal(0)  # Using Decimal for accurate financial calculations
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        # Fetch the subscription from the database
        subscription = get_object_or_404(User_Subscriptions, pk=item_id)
        
        # Since item_data is a dictionary, extract the relevant information
        vat = Decimal(item_data['vat'])
        cost = Decimal(item_data['cost'])
        total_cost = Decimal(item_data['total_cost'])
        total += cost  # Add the cost to the total
        product_count += 1  # Assuming only one item per cart as per your logic
        
        cart_items.append({
            'item_id': item_id,
            'subscription': subscription,  # Pass the actual subscription object
            'cost': cost,
            'total_cost': total_cost,
            'vat': vat,
            'auto_renew': item_data['auto_renew'],
            'image': item_data['image'],
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'vat': vat,
        'cost': cost,
        'total_cost': total_cost,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context