from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User_Profile
from .forms import CustomForm


# Create your views here.

def profile(request):
    """ A view to show subscriptions page """

#    form = CustomForm(instance=request.user)

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

#    if request.method == "POST":
#        form = CustomForm(request.POST, instance=request.user)
#        if form.is_valid():
#            form.save()

    context = {
        'current_path': current_path,
        'referrer': referrer,
#        'form': form,
    }

    return render(request, 'profiles/profile.html', context)

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
