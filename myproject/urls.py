from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [

    path('', views.HomeListView.as_view(), name='home'),

    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),

    path('admin/', admin.site.urls),

]