class MenuItem:
    def __init__(self, text, url):
        self.text = text
        self.url = url
    def __str__(self):
        return self.text +'  url:' + self.url

def make_menu():
    res = list()
    res.append(MenuItem("Главная", "/"))
    res.append(MenuItem("Навыки (на функциях)", "/view_skills"))
    res.append(MenuItem("Навыки (на классах)", "/skill_list"))
    res.append(MenuItem("Контакты", "/contacts"))
    return res

