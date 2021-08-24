# saidin_django_api
O um overview de uma api do django
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