from django.contrib import admin
from porfolio.models import *

admin.site.register(Client)

class MediaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}    

class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('name', 'completion_date', 'client', 'in_development', 'is_public')
    list_filter   = ('in_development', 'is_public', 'media')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Project, ProjectAdmin)