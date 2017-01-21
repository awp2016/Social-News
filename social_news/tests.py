from django.test import TestCase
from django.contrib.auth.models import User


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
        self.assertContains(response, 'Wrong username or password')

    def test_index_redirects_to_login(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/login?next=/')
