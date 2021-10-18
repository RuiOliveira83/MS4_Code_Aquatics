from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from random import choice
from .models import Post

from products.models import Product
from .forms import PostForm


def list_posts(request):
    posts = Post.objects.all()
    pks = Product.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_product = Product.objects.get(pk=random_pk)


    context = {
        'random_product': random_product,
        'posts': posts
    }

    return render(request, 'blog/list_posts.html', context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    pks = Product.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_product = Product.objects.get(pk=random_pk)

    context = {
        'random_product': random_product,
        'post': post
    }

    return render(request, 'blog/post/post_detail.html', context)


def add_post(request):
    """ Add a new blog post """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add post. '
                                    'Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form
    }

    return render(request, template, context)


def edit_post(request, slug):
    """ Edit a blog post """
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the blog post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request,
                           'Failed to update blog. '
                           'Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.slug}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)
