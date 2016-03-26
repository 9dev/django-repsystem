from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, TemplateView

from repsystem.utils import perform_action, get_user_history

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


class ReputationHistoryView(TemplateView):
    template_name = 'main/reputation_history.html'

    def get_context_data(self, **kwargs):
        context = super(ReputationHistoryView, self).get_context_data(**kwargs)
        context['history'] = get_user_history(self.request.user)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReputationHistoryView, self).dispatch(*args, **kwargs)
