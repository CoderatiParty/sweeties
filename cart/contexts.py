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
        auto_renew = False  # Default value for unauthenticated users

        if request.user.is_authenticated:
            try:
                # Fetch the user's subscription info if they are logged in
                subscription_info = Subscription_Info_For_User.objects.filter(
                    user_profile=request.user.user_profile,
                    subscription=subscription
                ).first()  # Use .first() to avoid 404 errors and get None if it doesn't exist
                if subscription_info:
                    auto_renew = subscription_info.auto_renew
            except Subscription_Info_For_User.DoesNotExist:
                pass

        # Since item_data is a dictionary, extract the relevant information
        cost = Decimal(item_data.get('cost', subscription.cost))
        total += cost  # Add the cost to the total
        product_count += 1  # Allow only one item per cart

        
        cart_items.append({
            'item_id': item_id,
            'subscription_type': item_data['subscription_type'],
            'desciption': 'description',
            'cost': cost,
            'duration_years': 'duration_years',
            'duration_days': 'duration_days',
            'subscription': subscription,
            'auto_renew': auto_renew,
            'image': 'image',
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