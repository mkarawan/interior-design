from .models import Category, Post


def my_context(request):

    cats = Category.objects.all()
    return {
        'cats': cats
    }