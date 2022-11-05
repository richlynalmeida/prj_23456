from django.contrib import admin
from . import models


#admin.site.register(models.Project)
admin.site.register(models.ProjectCalendar)
admin.site.register(models.CameoseDates)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_code', 'project_title', 'venue', 'comments', 'company',  'start_date', 'finish_date', 'id',)
    list_display_links = None

admin.site.register(models.Project, ProjectAdmin)