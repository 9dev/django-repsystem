from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^$',
        views.homepage,
        name='homepage'
    ),
    url(
        r'^create$',
        views.ArticleCreateView.as_view(),
        name='article_create'
    ),
    url(
        r'^article/(?P<pk>[0-9]+)',
        views.ArticleDetailView.as_view(),
        name='article_detail'
    ),
    url(
        r'^reputation_history$',
        views.ReputationHistoryView.as_view(),
        name='reputation_history'
    ),
]
