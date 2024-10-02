from decimal import Decimal, ROUND_HALF_UP
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
        product_count += 1  # Allow only one item per cart


        
        cart_items.append({
            'item_id': item_id,
            'type': item_data['type'],
            'desciption': 'description',
            'cost': cost,
            'duration_years': item_data['duration_years'],
            'duration_days': 'duration_days',
            'auto_renew': item_data['auto_renew'],
            'purchase_date': 'purchase_date',
            'renew_date': 'renew_date',
            'subscription': subscription,
            'image': item_data['image'],
        })

    vat_percentage = Decimal(settings.VAT_PERCENTAGE) / Decimal(100)
    vat_amount = vat_percentage * total
    vat_amount = vat_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    grand_total = total + vat_amount
    grand_total = grand_total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    context = {
        'cart_items': cart_items,
        'total': total,
        'vat_amount': vat_amount,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context