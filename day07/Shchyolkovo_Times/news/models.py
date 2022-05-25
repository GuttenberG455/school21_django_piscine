from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(("article title"), max_length=64, null=False)
    author = models.ForeignKey(User, verbose_name=(
        "article author"), on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(
        "article datetime created", auto_now=False, auto_now_add=True)
    synopsis = models.CharField(
        "article synopsis", max_length=312, null=False)
    content = models.TextField("article content")

    def __str__(self):
        return str(self.title)


class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(User, verbose_name=(
        "UserFavouriteArticle user"), on_delete=models.CASCADE, null=False)
    article = models.ForeignKey(Article, verbose_name=(
        "UserFavouriteArticle article"), on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.article.title)
