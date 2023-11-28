from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Episodes(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(width_field=400, height_field=500)
    tags = models.ManyToManyField('Tags')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name
