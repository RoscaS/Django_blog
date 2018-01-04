import forgery_py
from random import seed, randint

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

def _paragraph():
    p = forgery_py.lorem_ipsum.sentences(randint(4, 18))
    return f'<p>{p}</p><br>'

class Post(models.Model): 
    title = models.CharField(max_length=255)
    headline = models.CharField(max_length=400, blank=True)
    body  = models.TextField(max_length=None, null=True, blank=True)
    date  = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    author  = models.ForeignKey(User, related_name='posts', on_delete=None)
    
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=None)


    def __str__(self):
        return self.title

    def generate_fake(count=50):   
        seed()
        for i in range(count):
            Post.objects.create(
                title    = forgery_py.lorem_ipsum.words(randint(2,5)).capitalize(),
                headline = forgery_py.lorem_ipsum.sentence(),
                body     = ''.join([_paragraph() for i in range(randint(1, 4))]),
                author   = User.objects.get(username='RoscaS')
            )


class Comment(models.Model):
    body = models.TextField(max_length=4000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=None)
    post = models.ForeignKey(Post, related_name='comments', on_delete=None)

    def __str__(self):
        short = Truncator(self.body)
        return short.chars(30)



