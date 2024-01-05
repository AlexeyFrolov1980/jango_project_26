from django.contrib import admin
import blogapp.models
# Register your models here.

admin.site.register(blogapp.models.Area)
admin.site.register(blogapp.models.Skill)
admin.site.register(blogapp.models.Vacancy)

