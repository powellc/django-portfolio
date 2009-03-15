from django.contrib import admin
from portfolio.models import *

admin.site.register(Client)

class MediumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}    

admin.site.register(Medium, MediumAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('name', 'completion_date', 'client', 'in_development', 'is_public')
    list_filter   = ('in_development', 'is_public', 'media')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Project, ProjectAdmin)