from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='blog'),
    path('categories/<int:id>/', views.Categories.as_view(), name='categories'),
    path('article/<int:id>/', views.Article.as_view(), name='article'),
    path('about_me', views.AboutMe.as_view(), name='about_me'),
    path('projects', views.Projects.as_view(), name='projects'),
    path('contact', views.Contact.as_view(), name='contact'),

]
