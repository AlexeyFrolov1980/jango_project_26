import requests  # Для запросов по API
import json  # Для обработки полученных результатов


def get_areas():
    with requests.get('https://api.hh.ru/areas') as req:
        data = req.content.decode()

    jsobj = json.loads(data)
    areas = []
    for k in jsobj:
        for i in range(len(k['areas'])):
            if len(k['areas'][i]['areas']) != 0:  # Если у зоны есть внутренние зоны
                for j in range(len(k['areas'][i]['areas'])):
                    areas.append([k['id'],
                                  k['name'],
                                  k['areas'][i]['areas'][j]['id'],
                                  k['areas'][i]['areas'][j]['name']])
            else:  # Если у зоны нет внутренних зон
                areas.append([k['id'],
                              k['name'],
                              k['areas'][i]['id'],
                              k['areas'][i]['name']])
    return areas


def get_area_code(area_name : str,  areas=None):
    if areas is None:
        areas = get_areas()

    for a in areas:
        if area_name.lower() == str(a[3]).lower():
            return a[2]

    for a in areas:
        if area_name.lower() == str(a[1]).lower():
            return a[0]
    return ''


def get_area_code_from_vac(vac):
    return vac['area']['id']





def get_page(params, page=0):
    # Справочник для параметров GET-запроса
    params['page'] = page,  # Индекс страницы поиска на HH

    with requests.get('https://api.hh.ru/vacancies', params) as req:  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно

    return data


def make_params(ketwords, area_code, per_page=100):
    params = {
        'text': 'NAME:' + ketwords,  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': area_code,  # Поиск ощуществляется по вакансиям города Москва
        'page': 0,  # Индекс страницы поиска на HH
        'per_page': per_page  # Кол-во вакансий на 1 странице
    }
    return params



def get_salary_from_vac(vacancy_data:dict):
    s_from = None
    s_to = None
    s_cur = None

    if vacancy_data['salary'] is not None:
        s_from = vacancy_data['salary']['from']
        s_to = vacancy_data['salary']['to']
        s_cur = vacancy_data['salary']['currency']

    return s_from, s_to, s_cur





def get_vac_list(params, per_page=50, page=0):
    params['page'] = page
    params['per_page'] = per_page
    data = get_page(params, page)
    jsObj = json.loads(data)
    v_pages = jsObj['pages']
    # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
    vlst = jsObj['items']
    vacs = list()
    skills = dict()

    for vac in vlst:
        vacancy_data = requests.get(vac['url']).json()
        sk = vacancy_data['key_skills']
        vac_skills = list()

        for skill in sk:
            skills[skill['name']] = skill['name']
            vac_skills.append(skill['name'])

        s_from, s_to, s_cur = get_salary_from_vac(vacancy_data)

        vacs.append([vac['id'], vac['name'], s_from, s_to, s_cur, vac['url'],
                     get_area_code_from_vac(vac), vac_skills])

    return vacs, skills

'''
params = make_params("Python", 1)

vacs, skills = get_vac_list(params, 5)

print(get_areas())

print(vacs)
print(skills)
'''