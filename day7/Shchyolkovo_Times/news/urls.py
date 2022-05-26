from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    path('articles/', views.render_articles, name='render_articles'),
    path('publications/', views.render_publications, name='render_publications'),
    path('favourites/', views.render_favourites, name='render_favourites'),
    url(r'^details/(?P<id_article>\d+)$', views.render_detail, name='render_detail'),
    url(r'^add_to_favourites/(?P<id_article>\d+)$', views.add_to_favourite, name='add_to_favourite'),
    path('publish/', views.add_article, name='add_article')
]