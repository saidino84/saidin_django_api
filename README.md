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
[ * ] e como ficaria esses arquivos

```py
books/api/serializer.py

from rest_framework import serializers
from books import models



class Book(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'



books/api/viewsets.py

from rest_framework import viewsets
from books.api import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all() # refiro me a todos campos do meu model Books
    
```

# 5 O Proximo passo para fazer o nosso projecto funcionar 'e criando a nossa routa

>> olhando no nosso projecto library tem um arquivo urls.py e' com ele onde estam inclusas as  nossas rotas 
>> por padrao ele ja inclue uma rota de nome path('admin', admin.site.urls)

```py 
library/urls.py
# default settings

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

"""
importarei include from django.urls que por padrao ele importa so o path
else include ele tem como objectivo de incluir todas as rotas do seu app"""
#Modified

from django.contrib import admin
from django.urls import path, include
# vou criar um Router para incluir todas as rotas do meu projecto
# um arouta base so, e tudo isso so 'e possivel com rest_framwork
from rest_framework import routers
# importanto os meus viewsets
from books.api import viewsets as Booksviewsets
# Criando o roter
route =routers.DefaultRouter()

# registando o meu view set na url books commbasename Books

route.register(r"saidino-books", Booksviewsets.BooksViewSet, basename="MyBooks")

# e por fim mando o django registrar o meu viw set na primera rota deste projecto no index
urlpatterns = [
    path('admin/', admin.site.urls),
    # registanto o meu viewset na inicio do meu site {192.186.43.1:5000/}
    path('',include(route.urls))
]

```

# 6. PRONTOS API ESTA COMPLETADO E' SO FAZER AS MIGRACOES ao novo modelo criado e rodar o apps
>> python manage.py makemigrations
este comando fara migracoes para este modelo de Books

>> e depis falar para o banco de dados que ker incluir essas migrations no database

>>python manage.py migrate

e podes rodar avontade 
>>python manage.py runserver

```py
Revisando o codigo
"saidino_django_api\library\urls.py"
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
# importanto o meu bookviewset
from books.api import viewsets as booksets

# criando o router
route =routers.DefaultRouter()
# registando o meu viewset no roter  esta sera a rota que vai chamar o viewBooks 192.168.43.1:5000/saidino-books
route.register(r'saidin-book', booksets.BooksViewSet, basename='MBooks')

urlpatterns = [
    path('admin/', admin.site.urls),
    # registando omeu view no app do django na  rota / {127.0.0.1:8000/}
    path('',include(route.urls))
    
]




```