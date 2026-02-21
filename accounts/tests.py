from django.test import TestCase
from .models import CustomUser

from django.urls import reverse , resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = CustomUser
        user = User.objects.create_user(username = "testuser",email = "testuser@gmail.com",password = "testpass123")
        self.assertEqual(user.username , "testuser")
        self.assertEqual(user.email,"testuser@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = CustomUser
        admin_user = User.objects.create_superuser(
                username="testsuperuser",email="testsuperuser@gmail.com",password="testpass123"
                )
        self.assertEqual(admin_user.username , "testsuperuser")
        self.assertEqual(admin_user.email , "testsuperuser@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTest(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code , 200)
        self.assertTemplateUsed(self.response , "registration/signup.html")
        self.assertContains(self.response,"Sign Up")
        self.assertNotContains(self.response , "Hi im not in that page")
    
    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form,CustomUserCreationForm)
        self.assertContains(self.response , "csrfmiddlewaretoken")
    
    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__ , SignupPageView.as_view().__name__)
