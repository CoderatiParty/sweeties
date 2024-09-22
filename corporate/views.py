from django.shortcuts import render

# Create your views here.

def corporate(request):
    """ A view to show the main corporate page """

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    context = {
        'current_path': current_path,
        'referrer': referrer,
    }

    return render(request, 'corporate/corporate_page.html', context)


def about(request):
    """ A view to show the main corporate page """

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    context = {
        'current_path': current_path,
        'referrer': referrer,
    }

    return render(request, 'corporate/about.html', context)


def contact(request):
    """ A view to show the main corporate page """

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    context = {
        'current_path': current_path,
        'referrer': referrer,
    }

    return render(request, 'corporate/contact.html', context)


def faqs(request):
    """ A view to show the main corporate page """

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    context = {
        'current_path': current_path,
        'referrer': referrer,
    }

    return render(request, 'corporate/faqs.html', context)


def privacy(request):
    """ A view to show the main corporate page """

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    context = {
        'current_path': current_path,
        'referrer': referrer,
    }

    return render(request, 'corporate/privacy.html', context)


def terms(request):
    """ A view to show the main corporate page """

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')

    context = {
        'current_path': current_path,
        'referrer': referrer,
    }

    return render(request, 'corporate/terms.html', context)