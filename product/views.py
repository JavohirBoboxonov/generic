from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Book
from .serializer import *

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = ProductSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = ProductSerializer