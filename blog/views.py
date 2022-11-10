from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


class HomeView(TemplateView):
    template_name = 'blog/main.html'


class Category(TemplateView):
    template_name = 'blog/category.html'


class Article(TemplateView):
    template_name = 'blog/article.html'

class AboutMe(TemplateView):
    template_name = 'blog/aboutme.html'

class Projects(TemplateView):
    template_name = 'blog/projects.html'

class Contact(TemplateView):
    template_name = 'blog/contact.html'


