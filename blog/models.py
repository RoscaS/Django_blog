from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

class Post(models.Model): 
    title = models.CharField(max_length=255)
    body  = models.TextField(max_length=4000, null=True, blank=True)
    date  = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    user  = models.ForeignKey(User, related_name='posts', on_delete=None)

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField(max_length=4000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=None)
    post = models.ForeignKey(Post, related_name='comments', on_delete=None)

    def __str__(self):
        short = Truncator(self.body)
        return short.chars(30)
