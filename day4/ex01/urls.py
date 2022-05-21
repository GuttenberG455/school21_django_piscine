from django.urls import path
from ex01 import views
from django.conf.urls.static import static

urlpatterns = [
    path('django', views.render_django, name='render_django'),
    path('display', views.render_display, name='render_display'),
    path('templates', views.render_templates, name='render_templates')
]