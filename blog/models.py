import forgery_py
import requests

from random import seed, randint

from django.utils.html import mark_safe
from markdown import markdown

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

def _paragraph():
    p = forgery_py.lorem_ipsum.sentences(randint(4, 18))
    return f'<p>{p}</p><br>'

def _paragraph_md():
    response = requests.get('https://jaspervdj.be/lorem-markdownum/markdown.txt')
    return response.text

class Post(models.Model): 
    title = models.CharField(max_length=255)
    headline = models.CharField(max_length=400, blank=True)
    body  = models.TextField(max_length=None, null=True, blank=True)
    date  = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    author  = models.ForeignKey(User, related_name='posts', on_delete=None)
    
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=None)

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.body, safe_mode='escape'))

    def __str__(self):
        return self.title

    def generate_fake(count=50, md=False):   
        seed()
        users = [i.username for i in User.objects.all()]
        for i in range(count):
            content = requests.get('https://jaspervdj.be/lorem-markdownum/markdown.txt').text
            article = content.splitlines()

            Post.objects.create(
                title    = article[0].lstrip('# '),
                headline = article[2].lstrip('## '),
                body     = '\n'.join(articleq[5:]).capitalize(),
                author   = User.objects.get(username=users[randint(0, len(users)-1)])
            )


class Comment(models.Model):
    body = models.TextField(max_length=4000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=None)
    post = models.ForeignKey(Post, related_name='comments', on_delete=None)

    def __str__(self):
        short = Truncator(self.body)
        return short.chars(30)



