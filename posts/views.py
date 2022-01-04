from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user
from django.contrib import messages

from .forms import PostForm
from .models import Posts
from accounts.decorators import allowed_user


@allowed_user(allowed_roles=['admin'])
def index(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


@login_required
def post(request, id):
    post = Posts.objects.get(id=id)
    context = {'post': post}
    return render(request, 'post.html', context)


@login_required
def add_post(request):
    post = PostForm(request.POST or None)
    if post.is_valid():
        post.instance.author = request.user  # add current user as author of the post
        post.save()
        return redirect('index')
    context = {'post': post}
    return render(request, 'add_post.html', context)


@login_required
def update_post(request, id):
    post = get_object_or_404(Posts, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.instance.author != request.user:
        return redirect('index')
    if form.is_valid():
        form.save()
        return redirect('post')
    context = {'form': form}
    return render(request, 'update_post.html', context)


@login_required
def delete_post(request, id):
    post = get_object_or_404(Posts, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.instance.author != request.user:
        return redirect('index')
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    context = {'post': post}
    return render(request, 'delete_post.html', context)
