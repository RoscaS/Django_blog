from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('accounts.urls')),

    # path('', views.HomeListView.as_view(), name='home'),
    # path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),

    path('admin/', admin.site.urls),

]