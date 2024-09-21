from django.shortcuts import render, get_object_or_404
from .models import Article, Category

# Create your views here.


def index(request):
    """ A view to return the home page """
    articles = Article.objects.all().order_by('-date')
    categories = Category.objects.all().order_by('name')

    context = {
        'articles': articles,
        'categories': categories,
    }

    return render(request, 'home/index.html', context)


def article(request, article_id):
    """ A view to show each article in full """

    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'home/article.html', context)