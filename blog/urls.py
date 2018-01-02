from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [

    path(
        '', 
        views.HomeListView.as_view(template_name='blog/home.html'), 
        name='home'
    ),

    path(
        'post/<int:pk>', 
        views.PostDetailView.as_view(template_name='blog/post_detail.html'), 
        name='post_detail'
    ),



]