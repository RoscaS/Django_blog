from django.utils import timezone
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rolepermissions.mixins import HasPermissionsMixin

from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, FormView, \
    CreateView, UpdateView, DeleteView

from blog.models import Post
from blog.forms import ContactForm, PostForm


class HomeListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5
    queryset = Post.objects.order_by('-date')



class PostDetailView(DetailView):
    context_object_name = 'post'
    model = Post


@method_decorator(login_required, name='dispatch')
class ContactView(SuccessMessageMixin, FormView):
    form_class      = ContactForm
    success_url     = reverse_lazy('home')
    success_message = 'Thank you for your feedback!'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class NewPostView(SuccessMessageMixin, HasPermissionsMixin, CreateView):
    required_permission = 'create_post'
    model       = Post
    form_class  = PostForm
    success_message = 'Post successfully created'
    
    def form_valid(self, form):
        post = form.save(commit=False)
        form.instance.author = self.request.user
        post.save()
        self.success_url = f'/blog/post/{post.pk}'
        return super().form_valid(form)


class PostUpdateView(SuccessMessageMixin, UpdateView):
    # TODO Row based permission !

    model = Post
    fields = ('title', 'headline', 'body',)
    pk_url_kwarg = 'pk'
    context_object_name = 'post'
    success_message = 'Post successfully edited'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        
        self.success_url = f'/blog/post/{post.pk}'
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    # TODO Row based permission !

    model = Post
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')
    success_message = 'Post successfully deleted'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
