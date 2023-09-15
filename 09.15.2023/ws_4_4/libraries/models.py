from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.TextField()
    pubdate = models.DateField()
    price = models.IntegerField()
    adult = models.BooleanField()
    # isbn = models.CharField(max_length=20)
    # Category_name=models.CharField(max_length=20)
    # Category_id = models.IntegerField()
