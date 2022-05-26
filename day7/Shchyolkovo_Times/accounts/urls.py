from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.render_log_in, name='render_log_in'),
    path('signup/', views.render_sign_up, name='sign_up'),
    path('logout/', views.log_out, name='log_out'),
]