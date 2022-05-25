
from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.render_log_in, name='log_in'),
    path('signup/', views.render_sign_up, name='sign_up'),
]
