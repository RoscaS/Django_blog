from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import Post

class HomeListView(ListView):
    template_name       = 'home.html'
    model               = Post
    context_object_name = 'posts'
    paginate_by         = 5


class PostDetailView(DetailView):
    template_name       = 'post_detail.html'
    model               = Post
    context_object_name = 'post'
