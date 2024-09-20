from django.shortcuts import render
from .models import Article

# Create your views here.


def index(request):
    """ A view to return the index page """
    articles = Article.objects.all().order_by('-date')

    context = {
        'articles': articles,
    }

    return render(request, 'home/index.html', context)
