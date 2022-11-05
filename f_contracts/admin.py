from django.contrib import admin
from . import models
from django.forms.widgets import TextInput
from f_contracts.models import Contract
from django import forms

admin.site.register(models.ContractPricingStyle)
admin.site.register(models.ContractType)
# admin.site.register(models.Contract)
admin.site.register(models.ContractSecondaryInfo)
admin.site.register(models.ContractClauses)
admin.site.register(models.TrendTypes)


class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_code', 'contract_title', 'contract_type', 'contract_pricing_style',
                    'parent_contract', 'discipline', 'contract_tender_costs', 'contract_award_costs', 'start_date',
                    'finish_date', 'comments', 'id',)
    list_filter = ('contract_code', 'contract_title', 'contract_type', 'contract_pricing_style',
                   'parent_contract', 'discipline', 'contract_tender_costs', 'contract_award_costs', 'start_date',
                   'finish_date', 'comments', 'id',)
    # list_editable = ('claim_type_code', 'claim_type_title', 'comments',)
    list_display_links = ('contract_code', 'contract_title', 'contract_type', 'contract_pricing_style',
                          'parent_contract', 'discipline', 'contract_tender_costs', 'contract_award_costs',
                          'start_date', 'finish_date', 'comments', 'id',)
    search_fields = ('contract_code', 'contract_title', 'contract_type', 'contract_pricing_style',
                     'parent_contract', 'discipline', 'contract_tender_costs', 'contract_award_costs',
                     'start_date', 'finish_date', 'id',)
    ordering = ('contract_code', 'contract_title', 'contract_type', 'contract_pricing_style')
    list_per_page = 10
    # formfield_overrides = {models.MoneyField:{'widget':TextInput(attrs={'class': 'text-right'}),},}
    # formfield_overrides = {
    #     models.MoneyField: {
    #         'widget': forms.TextInput(attrs={'style': 'text-align:right;', }),
    #     },
    # }


admin.site.register(models.Contract, ContractAdmin)


admin.site.register(models.ContractAudit)
