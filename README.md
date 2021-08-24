# saidin_django_api
O um overview de uma api do django

# 1 FIRST STEPS
>> intalattion of django and django-restapi dependecie
```sh
source .venv/bin/activate
pip install django djangorestframework  

# inicianod um projecto de nome library
djang-admin startproject library . #in the same directory 

# e iniciando um app de nome books
django-admin startapp books
# THEN START YOUR APP
python3 manage.py runserver
# some warning will rise from default django database cos got not migrations so we create it

python3 manage.py migrate  # to migrate the database creating tables in our database

```

# 2 First configurations on project/settings find at library/settings.py

```py

# Application definition
'''by default django comes with these apps installed and sqlite instaled
    to add our app in this django project setting just add inside of this bellow list the name of yr app
    and so, we have installed djangorestframework we'll add it roo
'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
# adiciondo os meus apps
    'rest_framework',# aferamenta que baixei
    'books' #e nome do meu app 
]

```

# 3 Criando o modelo de books 

```py
"in books/models.py is there where i gonna create my models of my books app"

from django.db import models
from uuid import uuid4   # owesame library to generate random ids

# Create your models here.
class Book(models.Model):
    """[this is Books Model ] which has as atribute :
    id_book, {book is}
    title =book title
    author release_year, pages publishing_company and created_at [the date of creation of this book]

    Args:
        models ([type]): [description]
    """
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year =models.IntegerField()
    pages =models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


```

# 4 hence ower model has been created now we are going to dive into serializer and viewset

> pela boa pratica de programacoa criarei uma pasta api no directory do meu app books onde 
> tera o meu serializer e o meu viewset do mesmo