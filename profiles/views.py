from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User_Profile
from .forms import UserProfileForm
from django.contrib.auth.models import User
from checkout.models import Order
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User
from checkout.models import Order, OrderLineItem


# Create your views here.

@login_required
def profile(request):
    """ A view to show profile page """

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

    profile = get_object_or_404(User_Profile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    
    orders = profile.orders.all()

    for order in orders:
        # Assuming there's only one subscription info per order, we fetch the first match
        subscription_info = Subscription_Info_For_User.objects.filter(
            user_profile=user_profile,
            payment=order  # Link to the correct order/payment
        ).first()

        # Add the renew_date as an attribute of the order object
        order.renew_date = subscription_info.renew_date if subscription_info else None

    template = 'profiles/profile.html'

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, template, context)


@login_required
def subscription_history(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)
    order_line_items = OrderLineItem.objects.filter(order=order)
    subscriptions = [item.subscription for item in order_line_items]
    user = order.user_profile.user  # Access the user through the user_profile relationship
    profile = get_object_or_404(User_Profile, user=request.user)
    first_name = user.first_name
    last_name = user.last_name


    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'from_profile': True,
        'order': order,
        'profile': profile,
        'subscriptions': subscriptions,
        'order_line_items': order_line_items,
        'first_name': first_name,
        'last_name': last_name,
    }

    return render(request, template, context)
