from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Reader(models.Model):
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    reader_id=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        last_4_digits=self.reader_id.username[-4:]
        return "{}_{}-{}".format(self.first_name,last_4_digits,self.city)
