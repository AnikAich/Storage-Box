from django.http import response
from django.test import TestCase
 
from django.test import Client
# Create your tests here.
 
class TestViewResponse(TestCase):
    
    def setUp(self):
        self.c = Client()
 
    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
 
        response = self.c.get('/')
        self.assertEqual(response.status_code, 302)
 
    def test_upload_url(self):
        """
        Test upload url
        """
 
        response = self.c.get('/upload/')
        self.assertEqual(response.status_code, 200)