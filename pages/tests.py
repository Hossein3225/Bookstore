from django.test import TestCase , SimpleTestCase
from django.urls import reverse , resolve

from .views import HomePageView , AboutPageView
# Create your tests here.



class HomePageTest(SimpleTestCase):
    def test_url_exists_at_the_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code , 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code , 200)

    def test_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response,"home.html")

    def test_homepage_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response,"home page")
    def test_homepage_dose_not_cantains_incorrect_html(self):
        response = self.client.get("/")
        self.assertNotContains(response,"this is not in my site")

    def test_homepage_url_resolves_homepageview(self):
        view  = resolve("/")
        self.assertEqual(view.func.__name__ , HomePageView.as_view().__name__)

# class HomepageTests(SimpleTestCase):
#     def setUp(self): 
#         url = reverse("home")
#         self.response = self.client.get(url)
#     def test_url_exists_at_correct_location(self):
#         self.assertEqual(self.response.status_code, 200)
#     def test_homepage_template(self):
#         self.assertTemplateUsed(self.response, "home.html")
#     def test_homepage_contains_correct_html(self):
#         self.assertContains(self.response, "home page")
#     def test_homepage_does_not_contain_incorrect_html(self):
#         self.assertNotContains(self.response, "Hi there! I should not be on the page.")

class AbotPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)
    def test_url_exists_at_the_correct_location(self):
        self.assertEqual(self.response.status_code , 200)
    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response,"about.html")
    def test_abotpage_contain_correct_html(self):
        self.assertContains(self.response , "About Page")
    def test_aboutpage_dosenot_contain_incorrect_html(self):
        self.assertNotContains(self.response , " Hi im must doset in the page.")
    def test_aboutpage_url_resolves_AboutPageView(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__ , AboutPageView.as_view().__name__)