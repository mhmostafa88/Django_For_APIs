from django.shortcuts import render
from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer

# Create your views here.

# use ListAPIView to create a read-only endpoint
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer