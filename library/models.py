from email.mime import image
from turtle import ondrag
from unicodedata import category
from django.db import models
from Reader.models import Reader
import datetime
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=350)
    description=models.CharField(max_length=450)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.CharField(max_length=350)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    image=models.ImageField()
    category=models.CharField(max_length=220)

    def __str__(self):
        return self.name

class Issue(models.Model):
    reader=models.ForeignKey(Reader,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    issued=models.BooleanField(default=False)
    issued_at=models.DateTimeField(auto_now=False,null=True,blank=True)
    returned=models.BooleanField(default=False)
    return_date=models.DateTimeField(auto_now=False,auto_created=False,
    auto_now_add=False,null=True,blank=True)

    def __str__(self):
        return "{}_{} book issue request".format(self.reader,self.book)

    

