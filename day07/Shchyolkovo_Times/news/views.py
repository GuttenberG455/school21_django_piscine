from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import *
from news.models import *


def go_home(request):
    return redirect("render_articles")


def render_articles(request):
    news_list = reversed(Article.objects.all())
    form = AuthorizationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        if log_in(request, form):
            return redirect("go_home")
        else:
            return redirect("render_log_in")
    return render(request, "news/articles.html", locals())


def render_publications(request):
    news_list = reversed(Article.objects.all().filter(author__article=request.user.id))
    return render(request, "news/publications.html", locals())


def render_favourites(request):
    fav_list = UserFavouriteArticle.objects.all()
    news_list = Article.objects.all()
    return render(request, "news/favourites.html", locals())
