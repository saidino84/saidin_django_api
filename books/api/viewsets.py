from rest_framework import viewsets
from books.api import serializer
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.BooksSerializer
    queryset = models.Books.objects.all() # refiro me a todos campos do meu modelo Books
    