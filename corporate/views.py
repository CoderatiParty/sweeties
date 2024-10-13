from django.shortcuts import render, get_object_or_404
from profiles.models import User_Profile
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User

# Create your views here.

def corporate(request):
    """ A view to show the main corporate page """
    
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

    context = {
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'corporate/corporate_page.html', context)


def about(request):
    """ A view to show the main corporate page """

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

    context = {
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'corporate/about.html', context)


def contact(request):
    """ A view to show the main corporate page """

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

    context = {
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'corporate/contact.html', context)


def faqs(request):
    """ A view to show the main corporate page """

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

    context = {
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'corporate/faqs.html', context)


def privacy(request):
    """ A view to show the main corporate page """

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

    context = {
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'corporate/privacy.html', context)


def terms(request):
    """ A view to show the main corporate page """

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

    context = {
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'corporate/terms.html', context)


def payments(request):
    """ A view to show the main corporate page """

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

    context = {
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'corporate/payments.html', context)


def refunds(request):
    """ A view to show the main corporate page """

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

    context = {
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'corporate/refunds.html', context)