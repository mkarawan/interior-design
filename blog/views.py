from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from taggit.models import Tag
from blog.models import Post, Category


class HomeView(TemplateView):
    template_name = 'blog/main.html'
    def get(self, request):
        posts = Post.objects.all().order_by('-published')
        paginator = Paginator(posts, 4)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(1)
        return render(request, 'blog/main.html', context={'posts':page})


class Categories(TemplateView):
    template_name = 'blog/category.html'

    def get(self, request, slug):
        categories = Category.objects.all()
        category = Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=category).order_by('-published')
        paginator = Paginator(posts, 4)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(1)
        return render(request, 'blog/category.html', context={'category': category, 'posts': page, 'categories': categories})


class Article(View):
    def get(self, request, slug, tag_slug=None):
        post = Post.objects.get(slug=slug)
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
        paginator = Paginator(tag_posts, 4)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(1)
        return render(request, 'blog/tag.html', context={'posts': page, 'tag': tag, 'tag_posts': tag_posts})


