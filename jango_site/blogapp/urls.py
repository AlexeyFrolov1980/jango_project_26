

from django.urls import path
from blogapp import views

app_name='blogapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('create', views.create_vacancy, name='crate'),
    path('contacts', views.contacts, name='contacts'),
    path('vacancy/<str:id>/', views.view_vacancy, name='vacancy'),
]
