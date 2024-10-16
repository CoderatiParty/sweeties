from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Article, Category
from profiles.models import User_Profile
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddArticleForm


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


@login_required
def add_article(request):
    """ A route to add an article to the site """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only journos can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added article!')
            return redirect(reverse('home'))
        else:
            messages.error(request,
                           ('Failed to add article. '
                            'Please ensure the form is valid.'))
    else:
        form = AddArticleForm()

    template = 'home/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_article(request, article_id):
    """ A route to edit an article """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only journos can do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = AddArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated article!')
            return redirect(reverse('article', args=[article.id]))
        else:
            messages.error(request,
                           ('Failed to update article. '
                            'Please ensure the form is valid.'))
    else:
        form = AddArticleForm(instance=article)
        messages.info(request, f'You are editing {article.headline}')

    template = 'home/edit_article.html'
    context = {
        'form': form,
        'article': article,
    }

    return render(request, template, context)


@login_required
def delete_article(request, article_id):
    """ To delete an article from the site """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only journos can do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    messages.success(request, 'Article deleted!')
    return redirect(reverse('home'))