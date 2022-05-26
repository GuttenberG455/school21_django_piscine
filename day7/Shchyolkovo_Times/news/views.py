import datetime
from sqlite3 import DatabaseError

from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import *
from news.forms import ArticleForm
from news.models import *
from accounts.views import *


def go_home(request):
    return redirect("render_articles")


def render_articles(request):
    news_list = Article.objects.all().order_by('-created')
    form = AuthorizationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        if log_in(request, form):
            return redirect("go_home")
        else:
            return redirect("render_log_in")
    return render(request, "news/articles.html", locals())


def render_favourites(request):
    news_list = UserFavouriteArticle.objects.filter(user=request.user)
    len_list = len(list(UserFavouriteArticle.objects.filter(user=request.user)))
    return render(request, "news/favourites.html", locals())


def render_publications(request):
    form = AuthorizationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        if log_in(request, form):
            return redirect("render_publications")
    news_list = Article.objects.all().filter(author=request.user).order_by('-created')
    len_list = len(list((Article.objects.all().filter(author=request.user))))
    return render(request, "news/publications.html", locals())


def render_detail(request, id_article):
    form = AuthorizationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        if log_in(request, form):
            return redirect("render_detail", id_article)
    article = Article.objects.get(pk=id_article)
    return render(request, "news/details.html", locals())


def add_article(request):
    form = ArticleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            Article.objects.create(author=request.user, title=form['title'].value(), synopsis=form['synopsis'].value(),
                                   content=form['content'].value(), created=datetime.datetime.now())
            # form.save()
            return redirect("render_articles")
        else:
            return render(request, "news/add_article.html", locals())
    return render(request, "news/add_article.html", locals())


def add_to_favourite(request, id_article):
    fav_article = Article.objects.get(pk=id_article)
    fav_user = request.user
    is_in_favorites = len(list(UserFavouriteArticle.objects.filter(article=fav_article, user=fav_user)))
    if not is_in_favorites:
        try:
            UserFavouriteArticle.objects.create(user=request.user, article=fav_article)
            is_added = True
            return render(request, "news/add_to_favorites.html", locals())
        except DatabaseError as e:
            print(e)
    return render(request, "news/add_to_favorites.html", locals())
