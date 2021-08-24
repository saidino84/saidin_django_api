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
Thanks to !()[https://youtu.be/wtl8ZyCbTbg]

# 7 para acessar o delete update precisamos passar id do book cadastrado  
na routa 127.0.0.1:8000/
apresenta todos os dados /uma lista de json k tem dentro do banco de
pode -se cadatrar e entao pra modificalo precisaomos copiar o url e acessarmos o link
>> GET 127.0.0.1:5000/saidin-book/be97b95d-a576-4df0-9f65-5100acadd676/ 
aqui aparecem todas as opcoes deste book do id especificado
```json
[delete] [put] [patch] isso poderas fazer no navegador

{
    "id_book": "be97b95d-a576-4df0-9f65-5100acadd676",
    "title": "Brincando com aprogramacao",
    "author": "saidino",
    "release_year": 6,
    "pages": 17,
    "publishing_company": "Tylor Gang",
    "created_at": "2021-08-24T08:51:34.653345Z"
}
```

# 8 TESTANDO COM PYTHON
```py

from requests import post,get, delete

url ='http://192.168.43.66:8000/saidin-book/'
rs=get(url).json()

print('YOUR DATA')
print(rs)

try:
    input('vai fazer post')
    pos=post(url, data={
    "title": input('titulo'),
    "author": input('author ?'),
    "release_year": int(input('ano')),
    "pages": int(input('pages')),
    "publishing_company": "Tylor Gang",
     
})
    print('POST SUCESFULL')
    input('vai deletar')
    index=int(input(f'qual deles o deletas ? pk sao: {len(rs)}'))
    if index <=len(rs)-1:
        d=delete(url+rs[index].get("id_book") )
    
        print('Delete ok !')
    else:
        print('o id especificado nao foi encontrado')
    
except Exception as e:
    print(f'error {e}')
```


# 9 ADICIONANDO JWT NA API

>>pip intall djangorestframework-simplejwt

# 10 configurations iniciais

Feito a Intalacoa djangorestframework-simplejwt, adicionamos uma nova seccao /no arquivo de configuracoa do project

```py
 "saidin_django_api/library/settings.py"
 depos da AUTH_PASSWORD_VALIDATORS =[
     ....,
     ....
]
"WE ADD THAT restframework sessiomn/setting to our project"
REST_FRAMEWORK ={
    'DEFAULT_AUTHENTICATION_CLASSES':('rest_framework_simplejwt.authentication.JWTAuthentication')
}
NESTA SESSAO 'E ONDE AGENTE ADICIONA VARIAS CONFIGURATIONS DENTRO DO PROJECTO'
```

# 11 NEXT STEP 'E CRIAR UM Url onde sera responsavel para redirecionar os meus usuarios com asenha e o servidor me retornar um jwt
para comecar importamos duas Views de rest_framework_simplejwt 
```py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #Views  que vao me dar acesso ao token

"""Feito as importacoes (isso dentro do arquivo urls.py) adicionamos mais duas rotas no nosso
"""
urlpatterns =[
    path('admin/', admin.site.urls),
    path('',include(route.urls))
        ]

        "Alem destas rotas adicionarei outras views que sao rest k acabei de importa la"

urlpatterns =[
    path('admin/', admin.site.urls),
    # ------------
    path('token',TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    # -----------------------------
    path('',include(route.urls))
        ]
```

# 12 PARA TAL PRECISAMOS CRIAR UM SUPERUSER NO BANCO DE DADOS

>> python manage.py create superuser
username :admin
password: root (strong one)
>> portanto tendo criado o TokenObtainPairView e TokenRefreshView se formos a dar opest na rota:
```py
from requests import post
url='192.168.43.1:5000/token'
d=r.post('http://192.168.43.66:5000/token/',json={'username':'saidino','password':'root'})
print(d.json())
>>"""

{
    'refresh': 
'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyOTg5MjEyMCwianRpIjoiZDhiMDBiNzJmMGVmNDQwMDgxN2M2OWZiNGExZDNiOWQiLCJ1c2VyX2lkIjoxfQ.Z6dkQ_1TVOY9jOrN4nTeVortDyyaHAKC2k6Vf0eAH3g', 

'access': 
'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5ODA2MDIwLCJqdGkiOiJmYWEzOWFjNzY3NTc0NDZkODhiYWM1YzUwMzFlZGJiYyIsInVzZXJfaWQiOjF9.FO_zK-vIJ9I0HeeIpc0JuYj6acjKE6_jkbWZUoMiitM'
}
"""
#se ja tem um super usr n banco 
post(url, json={'username':'admin','password':'root'})

"it return an json with token refresh and access"
{
    "refresh":'jahuishsuasxzczazxxacatq8qoquqhdskhqwoihqqiiwuuq88691286r927wwdtsghhxrdrtsdg',
    "access":'u773yshhjxgguwexwhxhw8ewjeww8wud'
}


```
>>[ NOTA B ] A nossa tota de api ainda nao defeni como auteticavel de acesso para tal vou codar ai 

# CONFIGURANDO AMINHA ROTA DE ACESSO A API COMO ACESSIVEL COM Token

> como dizer ao servidor que rota/ deve ser autenticada (so acessada com token)

SO PRECISAMOS FAZER UMA COISA /MODIFICARMOS O NOSSO viewSet de book 
impoortando nesse mesmo arquivo o IsAuthenticated

```py
/books/api/viewsets.py
'antes  {sem authenticacoa}'
from rest_framework import viewsets
from books.api import serializer
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.BooksSerializer
    queryset = models.Books.objects.all() # refiro me a todos campos do meu modelo Books

'depois {tornando ela autheticavel}'

from rest_framework import viewsets
from books.api import serializer
from books import models

from rest_framework.permissions import IsAuthenticated

class BooksViewSet(viewsets.ModelViewSet):
    permission_class = (IsAuthenticated,)
    serializer_class = serializer.BooksSerializer
    queryset = models.Books.objects.all() # refiro me a todos campos do meu modelo Books
    
# BOOOM  Show de bolla vc nao fara requisicao mais no meu api sem estares autenticada

```

# Testando
```py
from requests import post,get
['TESTANDO]
url='localhost:5000/'
['first']
'get acess token from /api only if you are authenticated as user admin'
token=pos('localhost:5000/api/',json={'username';'saidino','password':'root'}).json()['access']

t=get(url,headers={"Content-Type": "application/json",'Authorization':f'Bear {token}'})
```