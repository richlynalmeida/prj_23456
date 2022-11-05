from django.contrib import admin
from . import models

# admin.site.register(models.UOMSystem)
# admin.site.register(models.UOM)
# admin.site.register(models.MilepostTemplate)
# admin.site.register(models.MilepostTemplateDetail)
admin.site.register(models.Boolean)
# admin.site.register(models.Audit)


class UOMSystemAdmin(admin.ModelAdmin):
    list_display = ('uom_system_code', 'uom_system_title', 'id',)
    list_filter = ('uom_system_code', 'uom_system_title', 'id',)
    list_editable = ('uom_system_code', 'uom_system_title', 'id',)
    list_display_links = None
    search_fields = ('uom_system_code', 'uom_system_title', 'id',)
    ordering = ('uom_system_code',)
    list_per_page = 10


admin.site.register(models.UOMSystem, UOMSystemAdmin)


class UOMAdmin(admin.ModelAdmin):
    list_display = ('uom_system', 'uom_code', 'uom_title', 'id',)
    list_filter = ('uom_system', 'uom_code', 'uom_title', 'id',)
    list_editable = ('uom_system', 'uom_code', 'uom_title', 'id',)
    list_display_links = None
    search_fields = ('uom_system', 'uom_code', 'uom_title', 'id',)
    ordering = ('uom_code',)
    list_per_page = 10


admin.site.register(models.UOM, UOMAdmin)


class MilepostTemplateAdmin(admin.ModelAdmin):
    list_display = ('milepost_template_code', 'milepost_template_title', 'comments', 'id',)
    list_filter = ('milepost_template_code', 'milepost_template_title', 'comments', 'id',)
    list_editable = ('milepost_template_code', 'milepost_template_title', 'comments', 'id',)
    list_display_links = None
    search_fields = ('milepost_template_code', 'milepost_template_title', 'comments', 'id',)
    ordering = ['milepost_template_code', ]
    list_per_page = 10


admin.site.register(models.MilepostTemplate, MilepostTemplateAdmin)


class MilepostTemplateDetailAdmin(admin.ModelAdmin):
    list_display = (
        'milepost_template', 'step_no', 'short_desc', 'long_desc', 'step_budget', 'step_cum_budget',
        'xref_tags_col_name_p',
        'xref_tags_col_name_e', 'comments', 'id',)
    list_filter = (
        'milepost_template', 'step_no', 'short_desc', 'long_desc', 'step_budget', 'step_cum_budget',
        'xref_tags_col_name_p',
        'xref_tags_col_name_e', 'comments', 'id',)
    list_editable = (
        'milepost_template', 'step_no', 'short_desc', 'long_desc', 'step_budget', 'step_cum_budget',
        'xref_tags_col_name_p',
        'xref_tags_col_name_e', 'comments', 'id',)
    list_display_links = None
    search_fields = (
        'milepost_template', 'step_no', 'short_desc', 'long_desc', 'step_budget', 'step_cum_budget',
        'xref_tags_col_name_p',
        'xref_tags_col_name_e', 'comments', 'id',)
    ordering = ['milepost_template', ]
    list_per_page = 10


admin.site.register(models.MilepostTemplateDetail, MilepostTemplateDetailAdmin)
