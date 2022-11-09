from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='blog'),
    path('ideas', views.Ideas.as_view(), name= 'ideas'),
    path('article', views.Article.as_view(), name= 'article'),
    path('advices', views.Advices.as_view(), name= 'advices'),
    path('garden', views.Garden.as_view(), name= 'garden'),
    path('diy', views.Diy.as_view(), name= 'diy'),

]