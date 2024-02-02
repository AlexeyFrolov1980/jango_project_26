from django.test import TestCase
from .models import Skill, Vacancy
from users_app.models import AppUser
# faker - простые данные, например случайное имя
from faker import Faker
# FactoryBoy - данные для конкретной модели django
# mixer - полностью создать fake модель
from mixer.backend.django import mixer


# Create your tests here.
class PostTestCase(TestCase):

    def setUp(self):
        skill = Skill.objects.create(name='TEST_SKILL')
        user = AppUser.objects.create_user(username='test_user', email='test@test.com', password='&HJGBN123jduhfjf')
        self.vac = Vacancy.objects.create(name='test_vacancy', vacancy_id='1234567890', user=user, skills=[skill])

    def test_has_skills(self):
        self.assertFalse(self.vac.has_skills())
