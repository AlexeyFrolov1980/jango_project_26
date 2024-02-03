from django.db import models
from users_app.models import AppUser


class ActiveManager(models.Manager):

    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)


class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Area(models.Model):
    # Id не надо, он уже сам появиться
    area_id = models.IntegerField()
    area_name = models.CharField(max_length=64)
    city_id = models.IntegerField(unique=True, primary_key=True)
    city_name = models.CharField(max_length=64)

    def __str__(self):
        res = str(self.area_id) + " " + str(self.area_name) + " " + str(self.city_id) + " " + str(self.city_name)
        return res


class Skill(IsActiveMixin):
    name = models.CharField(max_length=64, unique=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

        # Переопределение метода save

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Создаем профиль
        # Если провиль не создан
        print("Скилл сохранили ", self)


class Vacancy(models.Model):
    vacancy_id = models.CharField(max_length=16, unique=True)
    name = models.TextField()
    city_id = models.ForeignKey(Area, on_delete=models.PROTECT)
    salary_from = models.IntegerField(null=True)
    salary_to = models.IntegerField(null=True)
    salary_cur = models.CharField(max_length=16, null=True)
    vac_url = models.URLField(null=False)
    skills = models.ManyToManyField(Skill)

    def has_skills(self):
        return bool(self.skills)

    def __str__(self):
        res = str(self.vacancy_id) + " \n"
        res += str(self.name) + " \n"
        res += str(self.vac_url)

        return self.name
