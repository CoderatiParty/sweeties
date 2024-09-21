from django.shortcuts import render, get_object_or_404
from .models import Article, Category

# Create your views here.


def index(request):
    """ A view to return the home page """
    # Get all categories to display in the menu
    categories = Category.objects.all()

    # Check if the 'latest' parameter is present in the URL
    latest = request.GET.get('latest')

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
    }

    return render(request, 'home/index.html', context)


def article(request, article_id):
    """ A view to show each article in full """

    current_path = request.path
    referrer = request.META.get('HTTP_REFERER')


    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
        'current_path': current_path,
        'referrer': referrer,
    }

    return render(request, 'home/article.html', context)