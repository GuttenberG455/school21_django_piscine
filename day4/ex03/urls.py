from django.urls import path
from ex03 import views

urlpatterns = [
    path('', views.render_gradient)
]