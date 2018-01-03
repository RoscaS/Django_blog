from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')