from django.test import Client
from django.test import TestCase
from faker import Faker

from users_app.models import AppUser


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Что мы можем проверить
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

        # post зарос
        response = self.client.post('/contact/',
                                    {'name': self.fake.name(), 'message': self.fake.text(),
                                     'email': self.fake.email()})

        self.assertEqual(response.status_code, 302)

        # Какие данные передаются в контексте
        response = self.client.get('/')
        self.assertTrue('posts' in response.context)

    def test_login_required(self):
        AppUser.objects.create_user(username='test_user', email='test@test.com', password='&HJGBN123jduhfjf')
        # Он не вошел
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 302)

        # Логиним
        self.client.login(username='test_user', password='&HJGBN123jduhfjf')

        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)

