from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *


class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/authors.html'


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news/allnews.html'
    context_object_name = 'Posts'


class Post(DetailView):
    model = Post
    context_object_name = 'Post'
    queryset = Post.objects.filter()


# class Comment(DetailView):
#     model = Comment
#     context_object_name = 'Comments'
#     queryset = Comment.objects.filter()



