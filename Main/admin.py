from django.contrib import admin
from .models import Skill, Project, Education, Experience


# Register your models here.
class Project_admin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title', 'id', 'to_display']
    search_fields = ['title', 'id']


class Skill_admin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name', 'id', 'to_display', 'programming_language']
    search_fields = ['name', 'id']


admin.site.register(Project, Project_admin)

admin.site.register(Skill, Skill_admin)

admin.site.register(Education)

admin.site.register(Experience)
