from rest_framework import viewsets
from books.api import serializer
from books import models


# Aplicando a minha routa authenticada
from rest_framework.permissions import IsAuthenticated

class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) #Est classe ja sera Autenticada
    serializer_class = serializer.BooksSerializer
    queryset = models.Books.objects.all() # refiro me a todos campos do meu modelo Books
    