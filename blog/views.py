from django.shortcuts import render

from .models import Post


def list_posts(request):
    posts = Post.objects.all()

    return render(request, 'blog/list_posts.html', {'posts': posts})
