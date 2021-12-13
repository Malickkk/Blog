from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm
from .models import Posts
from .forms import blogForm


class index(ListView):
    model = Posts
    template_name = 'index.html'


class post(DetailView):
    model = Posts
    template_name = 'post.html'


class add_post(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = ['title', 'body', ]
