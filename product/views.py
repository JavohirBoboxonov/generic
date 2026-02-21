from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Book
from .serializer import *

# Ham ro'yxatni ko'rish, ham yangi kitob qo'shish uchun:
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = ProductSerializer

# Bitta kitobni ko'rish, o'zgartirish yoki o'chirish uchun:
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = ProductSerializer