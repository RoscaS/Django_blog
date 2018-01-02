from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView

from blog.models import Post
from .forms import ContactForm

class HomeListView(ListView):
    template_name       = 'home.html'
    model               = Post
    context_object_name = 'posts'
    paginate_by         = 5


class PostDetailView(DetailView):
    template_name       = 'post_detail.html'
    model               = Post
    context_object_name = 'post'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # form.send_email()
        return super.form_valid(form)
