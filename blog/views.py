from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'blog/main.html'


class Ideas(TemplateView):
    template_name = 'blog/ideas.html'


class Article(TemplateView):
    template_name = 'blog/article.html'
