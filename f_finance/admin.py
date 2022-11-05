from django.contrib import admin
from . import models


# Register your models here.
# admin.site.register(models.CBWPAccountsReceivable)
# admin.site.register(models.CBWPAccountsPayable)


class CBWPAccountsPayable(admin.ModelAdmin):
    list_display = ('calendar_date', 'ap_costs','comments', 'cbwp', 'id',)
    list_filter = ('calendar_date', 'ap_costs','comments', 'cbwp', 'id',)
    # list_editable = ('claim_type_code', 'claim_type_title',)
    list_display_links = ('calendar_date', 'ap_costs','comments', 'cbwp', 'id',)
    search_fields = ('calendar_date', 'ap_costs','comments', 'cbwp', 'id',)
    ordering =  ('calendar_date', 'ap_costs','comments', 'cbwp', 'id',)
    list_per_page = 10


admin.site.register(models.CBWPAccountsPayable, CBWPAccountsPayable)


class CBWPAccountsReceivable(admin.ModelAdmin):
    list_display = ('calendar_date', 'ar_costs','comments', 'cbwp', 'id',)
    list_filter = ('calendar_date', 'ar_costs','comments', 'cbwp', 'id',)
    # list_editable = ('claim_type_code', 'claim_type_title',)
    list_display_links = ('calendar_date', 'ar_costs','comments', 'cbwp', 'id',)
    search_fields = ('calendar_date', 'ar_costs','comments', 'cbwp', 'id',)
    ordering =  ('calendar_date', 'ar_costs','comments', 'cbwp', 'id',)
    list_per_page = 10


admin.site.register(models.CBWPAccountsReceivable, CBWPAccountsReceivable)