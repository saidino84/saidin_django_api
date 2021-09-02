"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""imports de definicao de url de images que farei upload"""
from django.conf.urls.static import static
from django.conf import settings


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #Views  que vao me dar acesso ao token


from rest_framework import routers
# importanto o meu bookviewset
from books.api import viewsets as booksets

# criando o router
route =routers.DefaultRouter()
# registando o meu viewset no roter
route.register(r'saidin-book', booksets.BooksViewSet, basename='MBooks')

urlpatterns = [
    path('admin/', admin.site.urls),
    # registando omeu view no app do django na  rota / {127.0.0.1:8000/}
     # ------------
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    # -----------------------------
    path('',include(route.urls)),
    # adicionando aminhas urls de images de upload
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

