from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'views')

admin.site.register(Post, PostAdmin)