from django.contrib import admin
from . import models


admin.site.register(models.CommodityTypeCameose)
admin.site.register(models.CommodityCameose)
admin.site.register(models.CommodityDetailCameose)
# admin.site.register(models.CommodityType)
admin.site.register(models.Commodity)
admin.site.register(models.CommodityDetail)


class CommodityTypeAdmin(admin.ModelAdmin):
    list_display = ('commodity_type_code', 'commodity_type_title', 'id',)
    list_filter = ('commodity_type_title', 'commodity_type_code',)
    # list_editable = ('claim_type_code', 'claim_type_title', 'comments',)
    list_display_links = ('commodity_type_code', 'commodity_type_title', 'id',)
    search_fields = ('commodity_type_code', 'commodity_type_title', 'id',)
    ordering = ('commodity_type_code', 'commodity_type_title', 'id',)
    list_per_page = 10


admin.site.register(models.CommodityType, CommodityTypeAdmin)