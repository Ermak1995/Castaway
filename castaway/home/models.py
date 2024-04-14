from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Episodes(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    description = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    tags = models.ManyToManyField('Tags', related_name='tags')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    # author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('episodes_detail', kwargs={"episode_id": self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Episodes'
        ordering = ["-time_create"]


class Tags(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_tags', kwargs={"tag_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Tags'






