from django import forms
from .models import Post

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    def send_email(self):
        print('\n\nSENDING EMAIL\n\n')


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), max_length=255)

    class Meta:
        model = Post
        fields = ['title', 'headline', 'body']

