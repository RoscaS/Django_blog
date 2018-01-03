from django.contrib import admin
from django.urls import path, include, reverse_lazy
from accounts import views as accounts_views
from blog import views as blog_views

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [

    path(
        'accounts/login/', 
        view=LoginView.as_view(
            template_name='accounts/login.html',
            success_url = '/',
        ),
        name='login'
    ),

    path(
        'accounts/logout/',
        view=LogoutView.as_view(
            next_page=reverse_lazy('login'),
        ),
        name='logout'
    ),
]