from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='pics')
    description= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)
    quantity=models.IntegerField()
    city=models.CharField(max_length=100)
