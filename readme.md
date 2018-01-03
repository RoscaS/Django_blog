# Temp
`{{ value|truncatechars:9 }}`
* [truncator in templates](https://stackoverflow.com/questions/5235994/django-template-tag-to-truncate-text)


# Quick tips

Why use `reverse_lazy` instead of `reverse`? The reason is that for all generic class-based views the urls are not loaded when the file is imported, so we have to use the lazy form of reverse to load them later when they’re available.

----------

The UserCreationForm does not provide an email field. But we can extend it.
Create a file named forms.py inside the accounts folder:

```py
# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
```

```py
# accounts/view.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name='accounts/signup.html'
```


# Tools
```
mkdir myproject
cd myproject
virtualenv venv -p python3.6
source venv/bin/activate
pip install django
```

```
django-admin startproject myproject
django-admin startapp firstapp
```

```
python manage makemigrations
python manage migrate
```

```
python manage.py createsuperuser
```


```py
User.objects.all()[0].delete()


>>> User.objects.create_user(username='sol', email='s@l.c', password='1234')

>>> User.objects.create_user(username='steph', email='s@f.c', password='1234')

>>> Post.objects.create(title='First post', body='Lorem ipsum', user=User.objects.get(username='sol'))

>>> Comment.objects.create(body='Yes, +1', user=User.objects.get(username='steph') post=Post.objects.first())

>>> Post.objects.all()[0].title
'First post'

>>> User.objects.get(username='RoscaS').posts.all()[0].title
'First post'

>>> User.objects.get(username='RoscaS').posts.all()[0].comments.all()[0].body
'Yes, +1'
```



# 0.1

## Needs

1. Posts
2. Comments
3. Users

Breaking those 3 things into the following:

1. Models(Database tables)
2. Views(actions on the models themselves - retrieve all, edit, create)
3. Templates(index templates, edit templates, create templates)

### 1 Models(Database tables)

1. Post
2. Comment
3. User

* A User can own 0 to MANY Posts
* A Post can have 0 to MANY Comments
* A User can have 0 to Many Comments

```
Post[
    title,
    body,
    views,
    date,
    user--->User
]

Comment[
    body,
    date,
    user--->User
    post--->Post   
]

User[
    email,
    username,
    password,
    first name
    last name
]
```


### 2 Views (actions)

* As a user of the system, you can **GET ALL** of the Posts
* As a user of the system, you can **CREATE** a Post
* As a user of the system, you can **EDIT** a Post
* As a user of the system, you can **DELETE** a Post
* As a user of the system, you can **GET ALL** of the Comments for a single Post
<br>
* As a user of the system, you can **CREATE** a Comment
* As a user of the system, you can **EDIT** a Comment
* As a user of the system, you can **DELETE** a Comment
<br>
* As a new person, you can **GET ALL** of the Posts
* As a new person, you can **SIGN UP** as a User
* As a new user, you can **LOGIN**
* As a new logged in User you can **LOGOUT**
* As a new logged in User you can **DELETE** your account
<br>
* ...

### 3 Templates

* Home (**GET ALL** of the Posts)
    * **LOGIN**
    * **SIGN UP**
    * **LOGOUT**
    * Profile
        * **DELETE** your account
    

# Urls provided by `auth`

```
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
```

# Allauth

## Github

* Client ID: `bb619d2e9e29bc30cf18`
* Client Secret: `97679f4c72b1ce43442f700e2a9b4ea19a24cda1`
