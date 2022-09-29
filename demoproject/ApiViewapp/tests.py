from django.test import TestCase
from django.urls import reverse,resolve
from rest_framework.test import APITestCase
from .views import *
# Create your tests here.


class UrlTestCase(TestCase):
    # def test_category_api_view(self):
    #     url = reverse('CategoryAPIView/')
    #     self.assertEqual(resolve(url).func.view_class,CategoryAPIView)
        

    def test_category_api_view(self):
        url = reverse('CategoryAPIView/',args=(1))
        self.assertEqual(resolve(url).func.view_class,CategoryAPIView)
        
# class ViewTestCase(APITestCase):
#     def test_create_category(self):
#         pass