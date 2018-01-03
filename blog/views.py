from django.shortcuts import render, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, FormView

from blog.models import Post
from blog.forms import ContactForm


class HomeListView(ListView):
    template_name       ='blog/home.html'
    model               = Post
    context_object_name = 'posts'
    paginate_by         = 5


class PostDetailView(DetailView):
    template_name       ='blog/post_detail.html'
    model               = Post
    context_object_name = 'post'


class ContactView(SuccessMessageMixin, FormView):
    template_name   ='blog/contact.html'
    form_class      = ContactForm
    success_url     = '/'
    success_message = 'Thank you for your feedback!'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)



