from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from taggit.models import Tag

from blog.models import Post, Category


class HomeView(TemplateView):
    template_name = 'blog/main.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['posts'] = Post.objects.all()

        return ctx


class Categories(TemplateView):
    template_name = 'blog/category.html'


    def get(self, request, id):
        categories = Category.objects.all()
        category = Category.objects.get(pk=id)
        posts = Post.objects.filter(category=category).order_by('-published')

        return render(request, 'blog/category.html', context={'category': category, 'posts': posts, 'categories': categories})


class Article(View):
    def get(self, request, id, tag_slug=None):
        post = Post.objects.get(pk=id)
        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            posts = post.filter(tags__in=[tag])
        return render(request, 'blog/article.html', context={'post': post, 'tag': tag})


class AboutMe(TemplateView):
    template_name = 'blog/aboutme.html'


class Projects(TemplateView):
    template_name = 'blog/projects.html'


class Contact(TemplateView):
    template_name = 'blog/contact.html'

class Tags(View):
    def get(self, request, tag_slug=None):
        posts = Post.objects.all()
        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            tag_posts = posts.filter(tags__in=[tag])
        return render(request, 'blog/tag.html', context={'posts': posts, 'tag': tag, 'tag_posts': tag_posts})

