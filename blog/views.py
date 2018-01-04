from django.utils import timezone

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
    context_object_name = 'posts'
    paginate_by         = 5
    queryset            = Post.objects.order_by('-date')


class PostDetailView(DetailView):
    model               = Post
    context_object_name = 'post'


@method_decorator(login_required, name='dispatch')
class ContactView(SuccessMessageMixin, FormView):
    form_class      = ContactForm
    success_url     = '/'
    success_message = 'Thank you for your feedback!'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class NewPostView(HasPermissionsMixin, CreateView):
    required_permission = 'create_post'
    model       = Post
    form_class  = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        form.instance.author = self.request.user
        post.save()
        return redirect('post_detail', pk=post.pk)


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'headline', 'body',)
    pk_url_kwarg = 'pk'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)


class PostDeleteView(DeleteView):
    model = Post
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')

