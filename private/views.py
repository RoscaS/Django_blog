from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User


class PrivateView(ListView):
    model = User
    context_object_name = 'users'
    # queryset = User.objects.all()
