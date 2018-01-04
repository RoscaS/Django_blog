from django.contrib import admin
from django.urls import path
from private import views

urlpatterns = [

    path(
        'home/',
        views.PrivateView.as_view(
            template_name='private/private_home.html'
        ),
        name='private_home'
    ),
]