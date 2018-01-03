from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView



class BlogLogin(LoginView):
    success_url = '/'
    success_message = 'poule'


class BlogLogout(LogoutView):
    pass
    

