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
    

