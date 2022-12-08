from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from blog.models import Post, Category


class HomeView(TemplateView):
    template_name = 'blog/main.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['posts'] = Post.objects.all()
        ctx['categories'] = Category.objects.all()

        return ctx


class Categories(TemplateView):
    template_name = 'blog/category.html'


    def get(self, request, id):
        categories = Category.objects.all()
        category = Category.objects.get(pk=id)
        posts = Post.objects.filter(category=category).order_by('-published')

        return render(request, 'blog/category.html', context={'category': category, 'posts': posts, 'categories': categories})


class Article(View):
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        return render(request, 'blog/article.html', context={'post': post})


class AboutMe(TemplateView):
    template_name = 'blog/aboutme.html'


class Projects(TemplateView):
    template_name = 'blog/projects.html'


class Contact(TemplateView):
    template_name = 'blog/contact.html'
