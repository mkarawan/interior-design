from .models import Category, Post, Comment
from django.db.models import Count


def my_context(request):
    popular_posts = Post.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')[:4]
    cats = Category.objects.all()
    popular_tags = Post.tags.most_common()[:10]
    return {
        'cats': cats,
        'popular_tags': popular_tags,
        'popular_posts': popular_posts
    }