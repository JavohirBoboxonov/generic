from rest_framework import serializers
from .models import *
class ProductSerializer(Product):
    class Meta:
        model = 'Product'
        fields = '_all__'