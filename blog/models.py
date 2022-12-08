from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='images')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

