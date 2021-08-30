from ..models import User
from django.test import TestCase, Client
from django.urls import reverse

class UserModelTests(TestCase):
    
    def test_create_user(self):
        user = User.objects.create_user(
            username='user_test',
            email='user_mail@example.com',
            password='passW0rd',        
        )
        self.assertEqual(user.username, 'user_test')
        self.assertEqual(user.email, 'user_mail@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        user = User.objects.create_superuser(
            username='user_test',
            email='user_mail@example.com',
            password='passW0rd',        
        )
        self.assertEqual(user.username, 'user_test')
        self.assertEqual(user.email, 'user_mail@example.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
