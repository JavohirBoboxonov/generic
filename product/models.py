from django.db import models

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=10, max_digits=3)