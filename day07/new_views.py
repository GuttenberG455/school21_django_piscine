def render_favourites(request):
    fav_list = UserFavouriteArticle.objects.all()
    news_list = Article.objects.all()
    return render(request, "news/favourites.html", locals())


def render_publications(request):
    news_list = reversed(Article.objects.all().filter(author=request.user))
    return render(request, "news/publications.html", locals())

def add_new_article(request):
    form = ArticleForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("articles")
        else:
            return render(request, "news/add_article", locals())
    return render(request, "news/add_article", locals())


def render_detail(request, id_article):
    article = Article.objects.get(pk=id_article)
    return render(request, "news/details", locals())

