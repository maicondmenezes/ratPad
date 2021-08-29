from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, resolve
from pages.models import *
from pages.views import *

class TestHomePageView(TestCase):

    def test_reverse_resolve(self):
        self.assertEqual( reverse('pages:home'), '/')
        self.assertEqual( resolve('/').view_name, 'pages:home' )

    def test_status_code(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(reverse('pages:home'))
        self.assertTemplateUsed(response, 'home.html')        


class TestAboutPageView(TestCase):

    def test_reverse_resolve(self):
        self.assertEqual( reverse('pages:about'), '/sobre/')
        self.assertEqual( resolve('/sobre/').view_name, 'pages:about' )

    def test_status_code(self):
        response = self.client.get(reverse('pages:about'))
        self.assertEqual(response.status_code, 200)
    
    def test_template(self):
        response = self.client.get(reverse('pages:about'))
        self.assertTemplateUsed(response, 'about.html')   
