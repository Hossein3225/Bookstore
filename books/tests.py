from django.test import TestCase
from django.urls import reverse
# Create your tests here.

from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Shahname",
            author = "Ferdowsi",
            price = "12.00",
            )
    
    def test_book_listing(self):
        self.assertEqual(self.book.title , "Shahname")
        self.assertEqual(self.book.author , "Ferdowsi")
        self.assertEqual(self.book.price , "12.00")
    
    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code , 200)
        self.assertContains(response , "Shahname")
        self.assertTemplateUsed(response , "books/book_list.html")
    
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/123")
        self.assertEqual(response.status_code , 200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response , "Shahname")
        self.assertTemplateUsed(response,"books/book_detail.html")