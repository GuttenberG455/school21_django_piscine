from django.urls import path
from ex02 import views

urlpatterns = [
    path('', views.render_form)
]