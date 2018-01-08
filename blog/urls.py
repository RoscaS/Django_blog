from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [

    path(
        '', 
        views.HomeListView.as_view(
            template_name='blog/home.html'
        ), 
        name='home'
    ),

    path(
        'post/<int:pk>', 
        views.PostDetailView.as_view(
            template_name='blog/post_detail.html'
        ), 
        name='post_detail'
    ),

    path(
        'contact/',
        views.ContactView.as_view(
            template_name='blog/contact.html'
        ),
        name='contact'
    ),

    path(
        'post/new/',
        views.NewPostView.as_view(
            template_name = 'blog/new_post.html'
        ),
        name='new_post'
    ),

    path(
        'post/edit/<int:pk>/',
        views.PostUpdateView.as_view(
            template_name = 'blog/edit_post.html'
        ),
        name='edit_post'
    ),

    path(
        'post/delete/<int:pk>/',
        views.PostDeleteView.as_view(
            template_name = 'blog/post_confirm_delete.html'
        ),
        name='delete_post'
    ),

    path(
        'profile/<int:pk>/',
        views.UserProfileDetailView.as_view(
            template_name = 'blog/user_profile.html'
        ),
        name='profile_page'
    ),

    path(
        'profile/edit/<int:pk>/',
        views.UserUpdateProfileView.as_view(
            template_name = 'blog/update_profile.html'
        ),
        name='update_profile'
    ),

]