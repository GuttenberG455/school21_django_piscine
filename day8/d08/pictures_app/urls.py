from django.urls import path

from pictures_app import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]