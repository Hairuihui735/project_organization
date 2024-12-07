from django.contrib import admin
from .models import Project, Tariff, Leader

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date', 'image')
    fields = ('title', 'description', 'start_date', 'end_date', 'image')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tariff)
admin.site.register(Leader)