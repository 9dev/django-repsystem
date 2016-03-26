from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from repsystem.utils import perform_action

from .models import Article


def homepage(request):
    return render(request, 'main/homepage.html')


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', )

    def form_valid(self, form):
        perform_action(self.request.user, 'article_published')
        return super(ArticleCreateView, self).form_valid(form)


class ArticleDetailView(DetailView):
    model = Article
