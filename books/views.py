from django.shortcuts import render
from django.views.generic import ListView , DeleteView
# Create your views here.
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"

class BookDetailView(DeleteView):
    model = Book
    template_name = "books/book_detail.html"
