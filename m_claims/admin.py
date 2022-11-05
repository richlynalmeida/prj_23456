from django.contrib import admin
from . import models


admin.site.register(models.CBWPClaimDetail)
admin.site.register(models.CBWPClaimDetailContractClauseReferences)


class ClaimTypeAdmin(admin.ModelAdmin):
    list_display = ('claim_type_code', 'claim_type_title', 'comments', 'id',)
    list_filter = ('claim_type_code', 'claim_type_title',)
    # list_editable = ('claim_type_code', 'claim_type_title', 'comments',)
    list_display_links = ('claim_type_code',)
    search_fields = ('claim_type_code', 'claim_type_title', 'comments',)
    ordering = ('claim_type_code', 'claim_type_title')
    list_per_page = 10


admin.site.register(models.ClaimType, ClaimTypeAdmin)


class ClaimRouteAdmin(admin.ModelAdmin):
    list_display = ('claim_route_code', 'claim_route_title', 'id',)
    list_filter = ('claim_route_code', 'claim_route_title',)
    # list_editable = ('claim_type_code', 'claim_type_title',)
    list_display_links = ('claim_route_code',)
    search_fields = ('claim_route_code', 'claim_route_title',)
    ordering = ('claim_route_code', 'claim_route_title')
    list_per_page = 10


admin.site.register(models.ClaimRoute, ClaimRouteAdmin)



