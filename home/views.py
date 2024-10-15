from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from profiles.models import User_Profile
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User


# Create your views here.


def index(request):
    """ A view to return the home page """
    subscription = User_Subscriptions.objects.all()
    categories = Category.objects.all()

    # Check if the 'latest' parameter is present in the URL
    latest = request.GET.get('latest')

    user_has_paid_subscription = False

    # Check if the user is authenticated
    if request.user.is_authenticated:
        user_profile = get_object_or_404(User_Profile, user=request.user)
        subscription_infos = Subscription_Info_For_User.objects.filter(user_profile=user_profile)
        # Check if the user has any paid subscriptions
        if subscription_infos.filter(paid=True).exists():
            user_has_paid_subscription = True

    if latest:
        # Fetch the 20 most recent articles ordered by 'date' in descending order
        articles = Article.objects.order_by('-date')[:8]
    else:
        # If not showing the latest, check if filtering by category
        category_id = request.GET.get('category')

        # Filter articles by category if category_id exists, otherwise show all articles
        if category_id:
            articles = Article.objects.filter(category_id=category_id).order_by('-date')
        else:
            articles = Article.objects.order_by('-date')

    # Pass both categories and filtered articles to the template
    context = {
        'categories': categories,
        'articles': articles,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'home/index.html', context)


def article(request, article_id):
    """ A view to show each article in full """

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


    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
        'current_path': current_path,
        'referrer': referrer,
        'user_has_paid_subscription': user_has_paid_subscription,
    }

    return render(request, 'home/article.html', context)