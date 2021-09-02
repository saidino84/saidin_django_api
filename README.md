# saidin_django_api
O um overview de uma api do django

# 1 FIRST STEPS
>> intalattion of django and django-restapi dependecie
```sh
configurar python3.7
com pyenv
curl https://pyenv.run | bash

read me in pyenv installer repository
pyenv versions  [to check python  versions in your system]
pyenv intall -list [to list version available to install]
source .venv/bin/activate
pip install django djangorestframework  
pyenv install 3.7.3 [i used 3.7.3]
python3 -v [check py version]

pyenv global 3.7.3 [to set global python variables]
to  back previously python system use pyenv global system

using pipenv
>>python3 -m pip install pipenv

pipenv shell
>>pip install django,djangorestframework,djangorestframework_simplejwt,django-heroku,pillow,requests

'generate requirements.txt'
>>pipenv lock -r > requirements.txt
'to unistall package'
>>pipenv uninstall <package-name>
'To remove the virtual environment'
>>pipenv --rm
'see dependecies'
>>pip graph
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
from requests import get,post
import os

os.system('clear')
url='http://192.168.43.66:5000/'
api_tokens=post(url+'token/',json={'username':'saidino','password':'root'})

# print(api_tokens.json())
def get_acess_token():
    acess_token=None
    if 'access' in api_tokens.json():
        print('yes got token sucessfully')
        print(f'{api_tokens.json()}'if 'y'in  input('what to see ? n/y') else '')
        acess_token=api_tokens.json()['access']

    else:
        print('no token found')
    return acess_token

def get_api_data(access_token):
    if access_token != None:
        data =get(url+'saidin-book/', headers={'Authorization':f'Bearer {access_token}'})
        print(data.json())

if __name__ =='__main__':
    api_key=get_acess_token()
    data =get_api_data(api_key)
```

# USANDO DART / FLUTTER PARA CONSUMER COM O MESMO METODO
- [ x ] adicionarei adependencia do dio nao depencies

```dart
import 'package:dio/dio.dart';

class Service {
  String url = 'http://192.168.43.66:5000/';
  Dio _dio = Dio();

  Future<String?> get_token() async {
    var _token = await _dio.post(url + "token/",
        data: {'username': 'saidino', 'password': 'root'});
    print(_token.data['access']);

    return await _token.data['access'];
  }

  show_data() async {
    var token = await get_token();
    print(" THE TOKEN RECEIED $token");
    if (token == null) {
      return '';
    }
    // Adicionando os headers dessa api para acessar
    _dio.options.headers['Authorization'] = 'Bearer $token';
    var data = await _dio.get(url + 'saidin-book/');
    print(data.data);
  }
}

main() {
  var service = Service();
  service.get_token();
  service.show_data();
}



```

# 3 PARTE INCLUINDO IMAGE NA NOSSA API E CRIANDO MAIS UMA COLUNA NO MODELO DE BOOK

Modicando o modelo de Book para adicionar campo de IMAGE
```py
from django.db import models
from uuid import uuid4


def upload_image_book(img_instance, filename):
    """para nao houver problemas de identificacoa de image
    sera assim 'kmk22jw82hsuaichqcaca7_imahe1.png'

    """
    return f'{img_instance.id_book}_{filename}'

# Create your models here.
class Books(models.Model):
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

    # ele pode ser branco [blank=True] se nao kser incluir image
    image =models.ImageField(upload_to=upload_image_book,blank=True, null=True)


```

# CONFIGURANDO CAMINHO PADRAO ONDE AS IMAGES ESTARAM GUARDADAS

no setting.py do project

```py
library/settings.py
no final do arquivo de settings adicionar a linha

depois do STATIC_URL='/static/'
'importamos o modulo os
'#o nome de url que estas images estaram uploads'
import os
MEDIA_URL='/media/' 

'ESTE ARMAZENA O CAMINHO DESSE URL de medias (o link) caminho absoluto desse media'

MEDIA_ROOT =os.path.join(BASE_DIR,'media')

STATIC_URL = '/static/'

 

'''apos definir estes paths preciso ir nas urls 
1- import some configs from django.conf'''
from django.conf.urls.static import static
from django.conf import settings

# e defenir os urls no final da lista de urlpatthern

urlpatterns = [
    path('admin/', admin.site.urls),
    # registando omeu view no app do django na  rota / {127.0.0.1:8000/}
     # ------------
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    # -----------------------------
    path('',include(route.urls))
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


```
>> pip install pillow [to work with images]
>> python manage.py makemigrations 
>> python manage.py migrate

>> python manage.py runserver 0:8000
```json
"http://192.168.43.66:8000/saidin-book/" 
retorna um json do tipo:
[
{
    "id_book": "a580741a-1c26-4c16-aaa4-8d7ca6d1989f",
    "title": "Custom view com flutter",
    "author": "Flutter way",
    "release_year": 2020,
    "pages": 3,
    "publishing_company": "tg flutter.io",
    "created_at": "2021-09-01T22:04:38.048966Z",
    "image": "http://192.168.43.66:8000/media/a580741a-1c26-4c16-aaa4-8d7ca6d1989f_Screenshot_20210516-082441_YouTube.jpg"
},
]
```

# 10 FAZENDO DEPLOY NO HEROKU
[https://www.youtube.com/watch?v=01iXLbvGcNE&list=PLcM_74VFgRhrZZf3b7PaK3xQlfQi3kEkg&index=2]
>> heroku login
heroku: Press any key to open up the browser to login or q to exit: 
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/3ec44a5d-2128-463f-8666-9220bb7a4e66?requestor=SFMyNTY.g2gDbQAAAA8xOTcuMjE4LjExMi4xMzFuBgCQPyelewFiAAFRgA.c_Mwx9B5hWY3a_qRKNip3B_u13cxlZIyeM1usZ3L_Ho
Logging in... done
Logged in as tylorguy2018@gmail.com

'CREATE HEROKU APP TO HOST YOUR PROJECT'
>> heroku create saidino-django-api
Creating ⬢ saidino-django-api... done
https://saidino-django-api.herokuapp.com/ | https://git.heroku.com/saidino-django-api.git

'feito ja esta criado um app   heroku e para este project precisamos configurar no project.setting.py
os ALLOWED_HOSTS=[
    "https://saidino-django-api.herokuapp.com"
]

Feito essas modifications preciso criar o Procfile no meu root BASE_DIR
e  escrever por dentro as especificacoes do gunicorn : nome-do-projeto.wsgi
'para encontrar nome do project django precisa bazar no settings ir ate ROOT_URLCONF='library.urls' pegar
este nome sem urls

# 12 Instalar dependecias do django-heroku 
assim ja vamos deixar o banco de dados local/ sqlite irei usar um database robusto k o
proprio heroku disponibiliza k 'e o postGrel
>> pip install django-heroku

import django-heroku  dentro settings do project
 e no fim da linha do mesmo adicione
 import django_heroku

'para dizer k vai usar tudo k esta local dentro do heroku'
 django_heroku.settings(locals()) 