from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from blog.models import Post

class PostList(ListView):
    model               = Post
    context_object_name = 'posts'
    template_name       = 'home.html'
    paginate_by         = 5
    queryset            = Post.objects.all()

class PostPage(ListView):
    model               = Post
    context_object_name = 'post'
    template_name       = 'post.html'
    paginate_by         = 10

    def get_context_data(self, **kwargs):
        pass
        


        
