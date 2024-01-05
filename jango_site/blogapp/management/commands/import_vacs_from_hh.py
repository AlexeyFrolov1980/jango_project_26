from django.core.management.base import BaseCommand
import hh_functions
from blogapp.models import Area, Vacancy, Skill

#python manage.py import_vacs_from_hh -k Python -r Москва -c 50


class Command(BaseCommand):
    help = 'Импорт первичного наполнения базы из hh\nПараметры: \n Ключевые слова  -k (например "Python") \nРегион -r ("Москва")\n Количество -c (50)'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("-k", nargs="+", type=str)
        parser.add_argument("-r", nargs="+", type=str)
        parser.add_argument("-c", nargs="+", type=str)


    def handle(self, *args, **options):
        keywords = " ".join(options['k'])
        area_name = " ".join(options['r'])
        count = " ".join(options['c'])

        area_code = hh_functions.get_area_code(area_name)
        print(area_code)

        if area_code == '':
            print('Регион не найден')
            return

        #Грузим справочник городоа

        areas = hh_functions.get_areas()
        for a in areas:
            try:
                area_obj = Area.objects.create(area_id = int(a[0]), area_name = a[1], city_id = int(a[2]), city_name = a[3])
                print(area_obj)
            except:
                pass
        

        params = hh_functions.make_params(keywords, int(area_code), count)
        vacs, skills = hh_functions.get_vac_list(params)

        print()

        #Грузим скилы
        for s in skills:
            try:
                skill_obj = Skill.objects.create(name=s)
                print(skill_obj)
            except:
                pass

        #Грузим вакансии
        for v in vacs:
            try:
                area_code_obj = Area.objects.get(city_id=v[6])
                vac_skills = v[7]
                vac_obj = Vacancy.objects.create(vacancy_id=v[0], name=v[1], salary_from=v[2], salary_to=v[3],
                                                 salary_cur=v[4], vac_url=v[5], city_id=area_code_obj)
                for v_s in vac_skills:
                    vac_obj.skills.add(Skill.objects.get(name=v_s))

                vac_obj.save()
            except:
                pass