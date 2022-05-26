from django.db import models

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=64, null=False)
    file = models.ImageField(null=False)
