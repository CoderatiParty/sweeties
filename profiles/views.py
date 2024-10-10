from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User_Profile
from .forms import UserProfileForm
from django.contrib.auth.models import User
from checkout.models import Order
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User


# Create your views here.

@login_required
def profile(request):
    """ A view to show profile page """

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    profile = get_object_or_404(User_Profile, user=request.user)
    subscription = Subscription_Info_For_User.objects.filter(user_profile=profile, paid=True).all()

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

    template = 'profiles/profile.html'

    context = {
        'form': form,
        'subscription': subscription,
        'orders': orders,
        'on_profile_page': True,
        'current_path': current_path,
        'referrer': referrer,
    }

    return render(request, template, context)

def subscription_history(request, order_number):

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'from_profile': True,
    }

    return render(request, template, context)
