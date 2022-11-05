from django.contrib import admin
from . import models

# admin.site.register(models.Department)
# admin.site.register(models.Discipline)
# admin.site.register(models.WBSLocation)
admin.site.register(models.CostTypeClass)
admin.site.register(models.CostType)
admin.site.register(models.FacilitySystem)
admin.site.register(models.FacilitySystemDetail)
admin.site.register(models.EBWPType)
admin.site.register(models.EBWPStatus)
admin.site.register(models.CBWPType)
admin.site.register(models.CBWPStatus)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_code', 'department_title', 'id',)
    list_filter = ('department_code', 'department_title', 'id',)
    list_editable = ()
    list_display_links = ('department_code', 'department_title', 'id',)
    search_fields = ('department_code', 'department_title', 'id',)
    ordering = ('department_code',)
    list_per_page = 10


admin.site.register(models.Department, DepartmentAdmin)


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('discipline_code', 'discipline_title', 'id',)
    list_filter = ('discipline_code', 'discipline_title', 'id',)
    list_editable = ()
    list_display_links = ('discipline_code', 'discipline_title', 'id',)
    search_fields = ('discipline_code', 'discipline_title', 'id',)
    ordering = ('discipline_code',)
    list_per_page = 10


admin.site.register(models.Discipline, DisciplineAdmin)


class WBSLocationAdmin(admin.ModelAdmin):
    list_display = ('wbs_location_code', 'wbs_location_title', 'id',)
    list_filter = ('wbs_location_code', 'wbs_location_title', 'id',)
    list_editable = ()
    list_display_links = ('wbs_location_code', 'wbs_location_title', 'id',)
    search_fields = ('wbs_location_code', 'wbs_location_title', 'id',)
    ordering = ('wbs_location_code',)
    list_per_page = 10


admin.site.register(models.WBSLocation, WBSLocationAdmin)
