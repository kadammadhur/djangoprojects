from django.db import models

# Create your models here.



class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    qty = models.IntegerField()
    publication = models.CharField(max_length=30)
    author = models.CharField(max_length=30)

    class Meta:
        db_table = 'BOOK_DETAILS'