import django.forms
from django import forms
from .models import Skill


class ContactsForm(django.forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')


class SkillForm(django.forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'