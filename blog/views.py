from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


class HomeView(TemplateView):
    template_name = 'blog/main.html'


class Ideas(TemplateView):
    template_name = 'blog/ideas.html'


class Article(TemplateView):
    template_name = 'blog/article.html'

class Advices(TemplateView):
    template_name = 'blog/advices.html'

class Garden(TemplateView):
    template_name = 'blog/garden.html'

class Diy(TemplateView):
    template_name = 'blog/diy.html'


