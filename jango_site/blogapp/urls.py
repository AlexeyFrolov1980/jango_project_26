

from django.urls import path
from blogapp import views

app_name='blogapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('create', views.create_vacancy, name='crate'),
    path('contacts', views.contacts, name='contacts'),
    path('create_skill', views.craate_skill, name='create_skill'),
    path('view_skills', views.view_skills, name='view_skills'),
    path('view_skill/<int:id>/', views.view_skill, name='view_skill'),
    path('edit_skill/<int:id>/', views.edit_skill, name='edit_skill'),
    path('vacancy/<str:id>/', views.view_vacancy, name='vacancy'),
    path('skill_list', views.SkillListView.as_view(), name='skill_list'),
    path('skill_detail/<int:id>/', views.SkillDetailView.as_view(), name='skill_detail'),
    path('skill_create', views.SkillCreateView.as_view(), name='skill_create'),
    path('skill_update/<int:pk>/', views.SkillUpdataView.as_view(), name='skill_update'),
    path('skill_delete/<int:pk>/', views.SkillDeleteView.as_view(), name='skill_delete'),

]
