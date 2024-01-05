from django.db import models


class Area(models.Model):
    # Id не надо, он уже сам появиться
    area_id = models.IntegerField()
    area_name = models.CharField(max_length=64)
    city_id = models.IntegerField(unique=True, primary_key=True)
    city_name = models.CharField(max_length=64)

    def __str__(self):
        res = str(self.area_id) + " " + str(self.area_name) + " " + str(self.city_id) + " " + str(self.city_name)
        return res


class Skill(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return str(self.name)


class Vacancy(models.Model):
    vacancy_id = models.CharField(max_length=16, unique=True)
    name = models.TextField()
    city_id = models.ForeignKey(Area, on_delete=models.PROTECT)
    salary_from = models.IntegerField(null=True)
    salary_to = models.IntegerField(null=True)
    salary_cur = models.CharField(max_length=16, null=True)
    vac_url = models.URLField(null=False)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        res = str(self.vacancy_id) + " \n"
        res += str(self.name) + " \n"
        res += str(self.vac_url)

        return self.name

