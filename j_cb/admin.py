from django.contrib import admin

from .models import CBWP, EBWP, CBWPNote, CBWPAttachment
from . import models
from f_finance.models import CBWPAccountsPayable, CBWPAccountsReceivable
from l_actuals.models import CBWPActuals
from k_quantum.models import CBWPQuantum
from m_claims.models import CBWPClaimDetail
from r_risk.models import Risks


admin.site.register(models.CBWPAudit)
admin.site.register(models.CBWPRaciInformation)
# admin.site.register(models.CBWPAttachment)
# admin.site.register(models.CBWPNote)
# admin.site.register(models.CBWP)


# class EBWPAdmin(admin.ModelAdmin):
#     inlines = [CBWPAdmin, ]
#
#
# admin.site.register(EBWP, EBWPAdmin)


class CBWPChangesAdmin(admin.ModelAdmin):
    list_display = ('change_no', 'title', 'cbwp', 'change_amount', 'comments', 'id',)
    list_filter = ('change_no', 'title', 'cbwp', 'change_amount', 'id',)
    # list_editable = ('claim_type_code', 'claim_type_title',)
    list_display_links = ('change_no', 'title', 'cbwp', 'change_amount', 'id',)
    search_fields = ('change_no', 'title', 'cbwp', 'change_amount', 'id',)
    ordering = ('change_no', 'title', 'cbwp', 'change_amount', 'id',)
    list_per_page = 10


admin.site.register(models.CBWPChanges, CBWPChangesAdmin)


class CBWPNoteInline(admin.StackedInline):
    model = CBWPNote


class CBWPAttachmentInline(admin.StackedInline):
    model = CBWPAttachment


class CBWPActualsInline(admin.TabularInline):
    model = CBWPActuals


class CBWPQuantumInline(admin.StackedInline):
    model = CBWPQuantum


class CBWPAccountsPayableInline(admin.StackedInline):
    model = CBWPAccountsPayable


class CBWPAccountsReceivableInline(admin.StackedInline):
    model = CBWPAccountsReceivable


class CBWPClaimDetailInline(admin.StackedInline):
    model = CBWPClaimDetail


class RisksInline(admin.StackedInline):
    model = Risks


class CBWPAdmin(admin.ModelAdmin):
    inlines = [ CBWPNoteInline, CBWPAttachmentInline, CBWPQuantumInline ,CBWPActualsInline, CBWPAccountsPayableInline,
                CBWPAccountsReceivableInline, CBWPClaimDetailInline, RisksInline ]


admin.site.register(CBWP, CBWPAdmin)