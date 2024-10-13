from decimal import Decimal, ROUND_HALF_UP
from django.conf import settings
from django.shortcuts import get_object_or_404
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User


def cart_contents(request):
    cart_items = []
    total = Decimal(0)  # Using Decimal for accurate financial calculations
    product_count = 0
    cart = request.session.get('cart', {})
    for item_id, item_data in cart.items():
        # Fetch the subscription from the database
        subscription = get_object_or_404(User_Subscriptions, pk=item_id)

        # Handle authenticated and unauthenticated users
        auto_renew = item_data.get('auto_renew', False)  # Default value for unauthenticated users

        subscription_type = item_data.get('subscription_type', subscription.subscription_type)
        cost = Decimal(item_data.get('cost', subscription.cost))
        description = item_data.get('description', subscription.description)
        duration_years = item_data.get('duration_years', subscription.duration_years)

        # Add subscription details to cart items
        cart_items.append({
            'item_id': item_id,
            'subscription_type': subscription_type,
            'cost': cost,
            'description': description,
            'duration_years': duration_years,
            'auto_renew': auto_renew,
            'image': subscription.image.url if subscription.image else None,
        })

        total += cost
        product_count += 1


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