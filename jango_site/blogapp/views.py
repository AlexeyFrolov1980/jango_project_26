from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import blogapp.sitemenu
from django.core.mail import send_mail
from .models import Vacancy, Skill, Area
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ContactsForm, SkillForm
from django.views.generic.base import ContextMixin
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


# Все что связано со скилами
def craate_skill(request):
    menu = blogapp.sitemenu.make_menu()
    if request.method == 'GET':
        form = SkillForm()
        return render(request, 'blogapp/create_skill.html', context={'menu': menu, 'form': form})

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('blogapp:view_skills'))


def view_skills(request):
    skills = Skill.objects.all()
    menu = blogapp.sitemenu.make_menu()
    return render(request, 'blogapp/skills_view.html', context={'menu': menu, 'skills': skills})


def view_skill(request, id):
    menu = blogapp.sitemenu.make_menu()
    skill = get_object_or_404(Skill, id=id)
    return render(request, 'blogapp/skill_view.html', context={'menu': menu, 'skill': skill})

def edit_skill(request, id):
    menu = blogapp.sitemenu.make_menu()
    skill = get_object_or_404(Skill, id=id)
    return render(request, 'blogapp/edit_skill.html', context={'menu': menu, 'skill': skill})



class NameContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['name'] = 'Теги'
        return context

class SkillListView(ListView):
    model = Skill
    template_name = 'blogapp/skill_list.html'
    context_object_name = 'skills'
    paginate_by = 20


    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        return Skill.ActiveManager.all()

# детальная информация
class SkillDetailView(DetailView, NameContextMixin):
    model = Skill
    template_name = 'blogapp/skill_detail.html'
    context_object_name = 'skill'

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.id = kwargs['id']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Skill, pk=self.id)


# создание тега
class SkillCreateView(CreateView, NameContextMixin):
    # form_class =
    fields = '__all__'
    model = Skill
    success_url = reverse_lazy('blogapp:skill_list')
    template_name = 'blogapp/skill_create.html'

    def post(self, request, *args, **kwargs):
        """
        Пришел пост запрос
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        return super().form_valid(form)

class SkillUpdataView(UpdateView):
    fields = '__all__'
    model = Skill
    success_url = reverse_lazy('blogapp:skill_list')
    template_name = 'blogapp/skill_update.html'



class SkillDeleteView(DeleteView):
    template_name = 'blogapp/skill_delete.html'
    model = Skill
    success_url = reverse_lazy('blogapp:skill_list')