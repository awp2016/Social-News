import json
import urllib2

from django.contrib.auth.models import User
from django.test import TestCase


class LoginViewTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='Iulia',
                                 password='secret')

    def test_login_successful(self):
        response = self.client.post(
            '/login/', {'username': 'Iulia',
                        'password': 'secret'})
        self.assertRedirects(response, '/')

    def test_login_failure(self):
        response = self.client.post(
            '/login/', {'username': 'Iulia',
                        'password': 'fail'})
        self.assertEquals(response.status_code, 200)
