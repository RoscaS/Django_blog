from django.shortcuts import render, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, FormView

from blog.models import Post
from blog.forms import ContactForm

# ########## Mixins ##########

# class CurrentPageMixin(DetailView):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['current'] = self.template_name
#         return context



# ########## Views ##########

class HomeListView(ListView):
    template_name       = 'home.html'
    model               = Post
    context_object_name = 'posts'
    paginate_by         = 5


class PostDetailView(DetailView):
    template_name       = 'post_detail.html'
    model               = Post
    context_object_name = 'post'


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'
    success_message = 'Thank you for your feedback!'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)



