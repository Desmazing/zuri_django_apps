from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255)
    text = models.TextField()
    author = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)


def get_absolute_url(self):
    return reverse('blog_details', args=[self.slug])


def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)


class Meta:
    ordering = ['created_date']

    def __unicode__(self):
        return self.title
    