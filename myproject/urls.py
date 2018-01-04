from django.contrib import admin
from django.urls import path, include
from blog.views import HomeListView

urlpatterns = [

    path('', HomeListView.as_view(template_name='blog/home.html')),

    path('blog/',     include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('private/',  include('private.urls')),

    path('admin/', admin.site.urls),
]