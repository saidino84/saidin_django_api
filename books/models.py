from django.db import models
from uuid import uuid4

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