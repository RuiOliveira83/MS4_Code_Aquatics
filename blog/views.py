from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from random import choice
from .models import Post

from products.models import Product
from .forms import PostForm


def list_posts(request):
    """ A view to show all posts and select a random product from products """
    posts = Post.objects.all()
    pks = Product.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_product = Product.objects.get(pk=random_pk)

    context = {
        'random_product': random_product,
        'posts': posts,
        'on_blog_page': True,
    }

    return render(request, 'blog/list_posts.html', context)


def post_detail(request, slug):
    """ A view to show a post and select a random product from products """
    post = Post.objects.get(slug=slug)
    pks = Product.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_product = Product.objects.get(pk=random_pk)

    context = {
        'random_product': random_product,
        'post': post,
        'on_blog_page': True,
    }
    return render(request, 'blog/post/post_detail.html', context)


@login_required
def add_post(request):
    """ Add a new blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

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


@login_required
def edit_post(request, slug):
    """ Edit a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

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


@login_required
def delete_post(request, slug):
    """ Delete a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    post = Post.objects.get(slug=slug)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
