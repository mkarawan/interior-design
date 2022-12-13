from .models import Category, Post


def my_context(request):

    cats = Category.objects.all()
    popular_tags = Post.tags.most_common()[:10]
    return {
        'cats': cats,
        'popular_tags': popular_tags
    }