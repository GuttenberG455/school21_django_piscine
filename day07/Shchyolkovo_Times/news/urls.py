from django.urls import path

from . import views


urlpatterns = [
    path('articles/', views.render_articles, name='render_articles'),
    path('publications/', views.render_publications(), name='render_publications'),

]