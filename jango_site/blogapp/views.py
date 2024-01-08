from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
import blogapp.sitemenu
from django.core.mail import send_mail
from blogapp.models import Vacancy, Skill, Area

from blogapp.forms import ContactsForm

# Create your views here.
def main_view(request):
    menu = blogapp.sitemenu.make_menu()

    return render(request, 'blogapp/index.html', context={'menu': menu})


def create_vacancy(request):
    menu = blogapp.sitemenu.make_menu()

    return render(request, 'blogapp/create.html', context={'menu': menu})

def contacts(request):
    menu = blogapp.sitemenu.make_menu()

    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            # Получить данные из форы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail(
                'Contact message',
                f'Уважаемый {name} Ваше сообщение {message} принято',
                'from@example.com',
                [email],
                fail_silently=True,
            )

            return HttpResponseRedirect('/')
        else:
            return render(request, 'blogapp/contacts.html', context={'menu': menu, 'form': form})
    else:
        form = ContactsForm()

        return render(request, 'blogapp/contacts.html', context={'menu': menu, 'form': form})

def view_vacancy(request, id):
    menu = blogapp.sitemenu.make_menu()

    vac = get_object_or_404(Vacancy, vacancy_id=id)

    return render(request, 'blogapp/vacancy.html', context={'menu': menu, 'id': id, 'vacancy': vac})



