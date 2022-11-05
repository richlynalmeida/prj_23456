from django.contrib import admin
from . import models
from .models import EBWPNote, EBWPAttachment, EBWP, EBWPCostDetails
from j_cb.models import CBWP
from i_eb.models import EBWP
from django.forms.widgets import TextInput, NumberInput

admin.site.register(models.EBWPAudit)
admin.site.register(models.EBWPRaciInformation)


# admin.site.register(models.EBWPAttachment)
# admin.site.register(models.EBWPNote)
# admin.site.register(models.EBWP)
# admin.site.register(models.OriginalEstimateBudget)
# # admin.site.register(models.CurrentEstimateBudget)

# class EBWPAdmin(admin.ModelAdmin):
#     list_display = ('ebwp_code', 'ebwp_title', 'ebwp_hours', 'ebwp_costs', 'id',)
#     fieldsets = [
#         ('Basic', {'fields': ['ebwp_status', 'ebwp_type', ]}),
#         ('WBS', {'fields': ['department', 'discipline', 'wbs_location', 'cost_type',
#                             'facility_system_detail', 'commodity_type', 'commodity', ]}),
#         ('Schedule', {'fields': ['eb_schedule', 'ebwp_discretionary_start_date',
#                                  'ebwp_discretionary_finish_date', ]}),
#         ('Contract', {'fields': ['contract', ]}),
#         ('EBWP Naming', {'fields': ['ebwp_code', 'ebwp_title', 'ebwp_sibling', ]}),
#         ('Scope', {'fields': ['uom', 'quantity', 'ebwp_hours', 'ebwp_costs', ]}),
#         ('Comments', {'fields': ['ebwp_comments', ]}),
#     ]
#     list_filter = ('ebwp_code', 'commodity_type',)
#     search_fields = ('ebwp_code', 'commodity_type',)
#     ordering = ('ebwp_code', 'commodity_type',)
#     # readonly_fields = ('ebwp_hours_ur',)
#     list_per_page = 10
#
#
# admin.site.register(models.EBWP, EBWPAdmin)


# class DatabaseViewsCEBTrendsInline(admin.StackedInline):
#     model = DatabaseViewsCEBTrends


class EBWPNoteInline(admin.StackedInline):
    model = EBWPNote


class EBWPAttachmentInline(admin.StackedInline):
    model = EBWPAttachment


class EBWPCostDetailsInline(admin.StackedInline):
    model = EBWPCostDetails


class CBWPInline(admin.StackedInline):
    model = CBWP


@admin.register(EBWP)
class EBWPAdmin(admin.ModelAdmin):
    list_display = ('ebwp_code', 'ebwp_title', 'quantity', 'ebwp_hours', 'ebwp_costs', 'id',)
    fieldsets = [
        ('EBWP Info.',
         {'fields': ['ebwp_code', 'ebwp_title', 'uom', 'quantity', 'ebwp_hours', 'ebwp_costs', 'contract',
                     'ebwp_status', 'ebwp_type', 'department', 'discipline', 'wbs_location', 'cost_type',
                     'facility_system_detail', 'commodity_type', 'commodity', 'eb_schedule',
                     'ebwp_discretionary_start_date', 'ebwp_discretionary_finish_date', 'ebwp_comments',
                     'ebwp_sibling', ]
          }
         ),
    ]
    list_filter = ('ebwp_code',)
    search_fields = ('ebwp_code',)
    ordering = ('ebwp_code',)
    list_per_page = 10

    # def formfield_for_db_field(self, ebwp_hours, request, **kwargs):
    #     field = super().formfield_for_dbfield(ebwp_hours, request, **kwargs)
    #     field.attrs.update({'class': 'text-right'})
    #     return field

    # # formfields for formatting
    # formfield_overrides = {
    #     models.DecimalInput: {'widget': TextInput(attrs={'class': 'text-right'}), }}

    # EBWP children using Inlines
    inlines = [EBWPCostDetailsInline, EBWPNoteInline, EBWPAttachmentInline, CBWPInline]

# admin.site.register(EBWP, EBWPAdmin)
