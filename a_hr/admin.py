from django.contrib import admin
from . import models
from .models import Company, CompanyCategory
import nested_admin


# class CompanyCategoryInline(nested_admin.TabularInline):
#     model = CompanyCategory
#     sortable_field_name = 'company_cat_code'
#     extra = 5
#
#
# class CompanyAdmin(admin.ModelAdmin):
#     model = Company
#     fieldsets = [('Company', {'fields':['company_code','company_title']})]
#     inlines = [CompanyCategoryInline]
#
#
# admin.site.register(Company, CompanyAdmin)


# class CompanyCategoryInline(nested_admin.NestedStackedInline):
#     model = CompanyCategory
#     sortable_field_name = 'company_cat_code'
#
#
# admin.site.register(models.CompanyCategory, CompanyCategoryInline)
#
#
# class CompanyInline(nested_admin.NestedStackedInline):
#     model = Company
#     sortable_field_name = 'company_code'
#     inlines = [CompanyCategoryInline]
#
#
# admin.site.register(models.Company, CompanyInline)


admin.site.register(models.Privilege)
admin.site.register(models.PersonnelCategory)
admin.site.register(CompanyCategory)
admin.site.register(Company)
admin.site.register(models.Personnel)
admin.site.register(models.StakeholderRoles)
admin.site.register(models.RaciMatrixDefinition)