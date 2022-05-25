# Generated by Django 3.2.13 on 2022-05-25 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='article title')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='article datetime created')),
                ('synopsis', models.CharField(max_length=312, verbose_name='article synopsis')),
                ('content', models.TextField(verbose_name='article content')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='article author')),
            ],
        ),
        migrations.CreateModel(
            name='UserFavouriteArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.article', verbose_name='UserFavouriteArticle article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='UserFavouriteArticle user')),
            ],
        ),
    ]