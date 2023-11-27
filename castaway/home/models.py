from django.db import models


class Episodes(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    tags = models.ManyToManyField('Tags')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ManyToManyField('Users')

