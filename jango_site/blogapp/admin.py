from django.contrib import admin
import blogapp.models


# Register your models here.
def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    actions = [set_active]

admin.site.register(blogapp.models.Area)
admin.site.register(blogapp.models.Vacancy)
admin.site.register(blogapp.models.Skill, SkillAdmin)

