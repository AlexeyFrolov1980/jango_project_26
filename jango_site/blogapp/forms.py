import django.forms
from django import forms

class ContactsForm(django.forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')
