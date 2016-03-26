from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from .models import Article


def homepage(request):
    return render(request, 'main/homepage.html')


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', )


class ArticleDetailView(DetailView):
    model = Article
