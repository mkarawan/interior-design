from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from taggit.models import Tag
from blog.models import Post, Category, Comment
from blog.forms import CommentForm
from django.contrib import messages
from django.shortcuts import redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import RequestContext



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
        return render(request, 'blog/main.html', context={'posts': page})


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
        comment_form = CommentForm()
        comments = post.comments.all()
        new_comment = None
        return render(request, 'blog/article.html', context={'post': post,
                                                              'comments': comments,
                                                              'new_comment': new_comment,
                                                              'comment_form': comment_form,
                                                              'tag': tag})

    def post(self, request, slug, tag_slug=None):
        post = Post.objects.get(slug=slug)
        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            posts = post.filter(tags__in=[tag])
        comment_form = CommentForm(request.POST)
        comments = post.comments.all()
        new_comment = None
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()
            messages.success(request, "Comment has been added!")
            return redirect(request.path_info)
        return render(request, 'blog/article.html', context={'post': post,
                                                              'comments': comments,
                                                              'new_comment': new_comment,
                                                              'comment_form': comment_form,
                                                              'tag': tag})

class AboutMe(TemplateView):
    template_name = 'blog/aboutme.html'


class Projects(TemplateView):
    template_name = 'blog/projects.html'


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = str(form.cleaned_data['email'])
#             message = form.cleaned_data['message']
#             send_mail(
#                 'New message from your website',
#                 f'From: {name}, Email: {email}, Message: {message}',
#                 email,
#                 ['settings.DEFAULT_FROM_EMAIL',],
#                 fail_silently=False,)
#             messages.success(request, "Email was sent!")
#             return redirect(request.path_info)
#     else:
#         form = ContactForm()
#     return render(request, 'blog/contact.html', {'form': form})
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Utwórz nowy obiekt EmailMessage
            email_message = EmailMessage(
                'New message from your website',
                strip_tags(render_to_string('blog/contact.html', {'name': name, 'email': email, 'message': message})),
                email, # adres e-mail nadawcy
                ['settings.DEFAULT_FROM_EMAIL'], # adres e-mail odbiorcy
            )
            email_message.encoding = 'utf-8' # opcjonalnie: użyj kodowania UTF-8
            try:
                email_message.send()
                messages.success(request, 'Wiadomość została wysłana.')
                return redirect(request.path_info)
            except:
                messages.warning(request, 'Wystąpił problem podczas wysyłania wiadomości.')
        else:
            messages.warning(request, 'Formularz jest niepoprawny.')

    else:
        form = ContactForm()
    context = {
        'form':form,
    }
    context = RequestContext(request, context)
    return render(request, 'blog/contact.html', context.flatten())


class Tags(View):
    def get(self, request, tag_slug=None):
        posts = Post.objects.all()
        tag = None
        tag_posts = posts
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            tag_posts = posts.filter(tags__in=[tag])
        paginator = Paginator(tag_posts, 4)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(1)
        return render(request, 'blog/tag.html', context={'posts': page, 'tag': tag})

class DeleteComment(View):
    def post(self, request, slug, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        post = comment.post
        comment.delete()
        messages.success(request, "Comment has been deleted!")
        return redirect('blog:article', slug=post.slug)

