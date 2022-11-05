from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from a_hr.models import Personnel, RaciMatrixDefinition
from b_wbs.models import CostType, Department, Discipline, WBSLocation, FacilitySystemDetail, CBWPType, CBWPStatus
from e_commodities.models import CommodityType, Commodity
from f_contracts.models import Contract, TrendTypes
from g_measures.models import UOM
from h_schedules.models import CBSchedule
from i_eb.models import EBWP
from d_mm.models import PurchaseOrder


class CurrentControlBudgetTrends(models.Model):
    tm_oeb_id = models.IntegerField(verbose_name='CBWP ID', default=1)
    ccb_trend_type = models.ForeignKey(TrendTypes, on_delete=models.CASCADE, verbose_name='CCB Trend Type ID',
                                       default=1)
    ccb_trend_qty = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                        verbose_name='CCB Trend Quantity')
    ccb_trend_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CCB UOM ID', default=1)
    ccb_trend_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                          verbose_name='CCB Trend Hours', default=0)
    ccb_trend_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                          verbose_name='CCB Trend Costs')
    ccb_trend_code = models.CharField(unique=True, max_length=55, verbose_name='CCB Trend Code')
    ccb_trend_title = models.CharField(unique=True, max_length=200, blank=True, null=True,
                                       verbose_name='CCB Trend Title')
    ccb_trend_comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CCB Trend Comments')
    ccb_approval_check = models.IntegerField(default=0, verbose_name='Approval Check')

    class Meta:
        managed = True
        verbose_name_plural = "Current Estimate Budget Trends"
        db_table = 'tm_ccb_trends'
        app_label = 'j_cb'
        ordering = ['ccb_trend_code']

    def __str__(self):
        return f"{self.ccb_trend_code} - {self.ccb_trend_title}"


class CurrentForecastBudgetTrends(models.Model):
    tm_oeb_id = models.IntegerField(verbose_name='CBWP ID', default=1)
    cfb_trend_type = models.ForeignKey(TrendTypes, on_delete=models.CASCADE, verbose_name='CFB Trend Type ID',
                                       default=1)
    cfb_trend_qty = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                        verbose_name='CFB Trend Quantity')
    cfb_trend_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CFB UOM ID', default=1)
    cfb_trend_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                          verbose_name='CFB Trend Hours', default=0)
    cfb_trend_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                          verbose_name='CFB Trend Costs')
    cfb_trend_code = models.CharField(unique=True, max_length=55, verbose_name='CFB Trend Code')
    cfb_trend_title = models.CharField(unique=True, max_length=200, blank=True, null=True,
                                       verbose_name='CFB Trend Title')
    cfb_trend_comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CFB Trend Comments')
    cfb_approval_check = models.IntegerField(default=0, verbose_name='Approval Check')

    class Meta:
        managed = True
        verbose_name_plural = "Current Forecast Budget Trends"
        db_table = 'tm_cfb_trends'
        app_label = 'j_cb'
        ordering = ['cfb_trend_code']

    def __str__(self):
        return f"{self.cfb_trend_code} - {self.cfb_trend_title}"


class CBWP(models.Model):
    cbwp_code = models.CharField(unique=True, max_length=55, verbose_name='CBWP Code')
    cbwp_title = models.CharField(unique=True, max_length=200, blank=True, null=True, verbose_name='CBWP Title')
    cbwp_status = models.ForeignKey(CBWPStatus, on_delete=models.CASCADE, verbose_name='CBWP Status ID',
                                    default=1)
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE, verbose_name='CBWP Cost Type ID',
                                  default=1)
    cbwp_type = models.ForeignKey(CBWPType, on_delete=models.CASCADE, verbose_name='CBWP Type ID',
                                  default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   verbose_name='CBWP Department ID', default=1)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE,
                                   verbose_name='CBWP Discipline ID', default=1)
    wbs_location = models.ForeignKey(WBSLocation, verbose_name='WBS Location ID', on_delete=models.CASCADE,
                                     default=1)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE,
                                 verbose_name='CBWP Contract ID', default=1)
    commodity_type = models.ForeignKey(CommodityType, on_delete=models.CASCADE,
                                       verbose_name='CBWP Commodity Type ID', default=1)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE,
                                  verbose_name='CBWP Commodity ID', default=1)
    facility_system_detail = models.ForeignKey(FacilitySystemDetail, on_delete=models.CASCADE,
                                               verbose_name='CBWP Facility System Detail ID', default=1)
    cb_schedule = models.ForeignKey(CBSchedule, on_delete=models.CASCADE,
                                    verbose_name='CBWP Schedule Activity Code', default=1)
    cbwp_discretionary_start_date = models.DateTimeField(blank=True, null=True,
                                                         verbose_name='CBWP Discretionary Start Date')
    cbwp_discretionary_finish_date = models.DateTimeField(blank=True, null=True,
                                                          verbose_name='CBWP Discretionary Finish Date')
    ebwp_parent = models.ForeignKey(EBWP, on_delete=models.CASCADE,
                                    verbose_name='EBWP Parent ID', null=True, blank=True, default=1)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE,
                                       verbose_name='Purchase Order ID', null=True, blank=True, default=1)
    # General comments for the CBWP
    cbwp_comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CBWP Comments')
    cbwp_primary_contact = models.CharField(unique=False, max_length=100, blank=True, null=True,
                                            verbose_name='CBWP Primary Contact or Owner')
    cbwp_secondary_contact = models.CharField(unique=False, max_length=100, blank=True, null=True,
                                              verbose_name='CBWP Secondary Contact')
    # Quantification, Pricing, Hours and Costs
    quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='CBWP Quantity')
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CBWP UOM ID', default=1)
    cbwp_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                     verbose_name='CBWP Hours', default=0)
    # The original budget of the Work Package - aka BAC (Budget At Completion), Control Budget (CB)
    cbwp_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                     verbose_name='CBWP Costs')
    cbwp_commit_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                            verbose_name='CBWP commitment Costs')
    # Costs to Manage Financial aspects
    # Receivables, also referred to as accounts receivable, are debts owed to a company by its customers
    # for goods or services that have been delivered or used but not yet paid for.
    # cbwp_receivables_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                              verbose_name='CBWP Receivable Costs')
    # Accounts payable refers to the money a company owes its suppliers for goods and services
    # that have been provided and for which the supplier has submitted an invoice.
    # cbwp_payables_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                           verbose_name='CBWP Payable Costs')
    # Placeholder costs is a number to manage the CBWP for any number of reasons (to provide flexibility)
    cbwp_placeholder_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                 verbose_name='CBWP Placeholder Costs')
    cbwp_placeholder_costs_comments = models.CharField(max_length=100, blank=True, null=True,
                                                       verbose_name='CBWP Placeholder Cost Comments')

    class Meta:
        managed = True
        verbose_name_plural = "CBWP Details"
        db_table = 'cbwp'
        app_label = 'j_cb'
        ordering = ['cbwp_code']

    def __str__(self):
        return f"{self.cbwp_code} - {self.cbwp_title}"


class CBWPAudit(models.Model):
    cbwp_id = models.IntegerField(verbose_name='CBWP ID')
    cbwp_code = models.CharField(max_length=55, verbose_name='CBWP Code')
    cbwp_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='CBWP Title')
    cbwp_status_id = models.IntegerField(verbose_name='EB Status ID')
    cost_type_id = models.IntegerField(verbose_name='Cost Type ID')
    cbwp_type_id = models.IntegerField(verbose_name='EB Type ID')
    department_id = models.IntegerField(verbose_name='Department ID')
    discipline_id = models.IntegerField(verbose_name='Discipline ID')
    wbs_location_id = models.IntegerField(verbose_name='WBS Location ID')
    contract_id = models.IntegerField(verbose_name='CBWP Contract ID')
    commodity_type_id = models.IntegerField(verbose_name='CBWP Commodity Type ID')
    commodity_id = models.IntegerField(verbose_name='CBWP Commodity ID')
    facility_system_detail_id = models.IntegerField(verbose_name='CBWP Facility System Detail ID')
    cb_schedule_id = models.IntegerField(verbose_name='CB Schedule ID')
    cbwp_discretionary_start_date = models.DateTimeField(blank=True, null=True,
                                                         verbose_name='CBWP Discretionary Start Date')
    cbwp_discretionary_finish_date = models.DateTimeField(blank=True, null=True,
                                                          verbose_name='CBWP Discretionary Finish Date')
    ebwp_parent_id = models.IntegerField(verbose_name='EB Sibling ID', blank=True, null=True)
    purchase_order_id = models.IntegerField(verbose_name='Purchase Order ID', blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='CBWP Quantity')
    uom_id = models.IntegerField(verbose_name='CBWP UOM ID')
    cbwp_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                     verbose_name='CBWP Hours')
    cbwp_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                     verbose_name='CBWP Costs')
    cbwp_commit_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                            verbose_name='CBWP Commitment Costs')
    # cbwp_receivables_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                              verbose_name='CBWP Receivable Costs')
    # cbwp_payables_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                           verbose_name='CBWP Payable Costs')
    cbwp_placeholder_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                 verbose_name='CBWP Forecast To Go Costs')
    cbwp_placeholder_costs_comments = models.CharField(max_length=100, blank=True, null=True,
                                                       verbose_name='CBWP Placeholder Cost Comments')
    cbwp_comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CBWP Comments')
    cbwp_primary_contact = models.CharField(max_length=2000, blank=True, null=True,
                                            verbose_name='CBWP Primary Contact or Owner')
    cbwp_secondary_contact = models.CharField(max_length=2000, blank=True, null=True,
                                              verbose_name='CBWP Secondary Contact or Owner')
    dml_action = models.CharField(max_length=2000, blank=True, null=True, verbose_name='DML Action')
    modified_by = models.CharField(unique=False, max_length=55, verbose_name='Modified By')
    modified_date = models.DateTimeField(unique=False, verbose_name='Modified Date')

    class Meta:
        managed = True
        verbose_name_plural = "CBWP Details - Audit"
        db_table = 'cbwp_audit'
        app_label = 'j_cb'
        ordering = ['cbwp_code']

    def __str__(self):
        return str('%s' % self.cbwp_code)


class CBWPRaciInformation(models.Model):
    cbwp = models.ForeignKey(CBWP, verbose_name='CBWP ID', on_delete=models.CASCADE)
    personnel = models.ForeignKey(Personnel, verbose_name='Personnel ID', on_delete=models.CASCADE)
    raci = models.ForeignKey(RaciMatrixDefinition, verbose_name='Raci Matrix Def ID', on_delete=models.CASCADE)
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='CBWP Raci Info Comments')

    class Meta:
        managed = True
        verbose_name_plural = "CBWP RACI Information"
        db_table = 'cbwp_raci_info'
        app_label = 'j_cb'
        unique_together = ['cbwp', 'personnel', 'raci']


class CBWPAttachment(models.Model):
    cbwp = models.ForeignKey(CBWP, on_delete=models.CASCADE, verbose_name='CBWP ID', default=1)
    attachment_code = models.CharField(unique=True, max_length=100, verbose_name='Attachment Code')
    attachment_title = models.CharField(max_length=100, verbose_name='Attachment Title')
    revision_number = models.CharField(max_length=3, blank=True, null=True, verbose_name='Revision No')
    revision_status = models.CharField(max_length=55, blank=True, null=True, verbose_name='Revision Status')
    release_date = models.DateTimeField(blank=True, null=True, verbose_name='Release Date')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='CBWP Attachment Comments')
    cbwp_attachment = models.FileField(blank=True, null=True, upload_to='CBWPAttachments/',
                                       verbose_name='CBWP Attachments')
    cbwp_url = models.URLField(blank=True, null=True, max_length=250, verbose_name='CBWP URL')

    class Meta:
        managed = True
        verbose_name_plural = 'CBWP Attachments'
        db_table = 'cbwp_attachment'
        app_label = 'j_cb'
        ordering = ['attachment_code']

    def __str__(self):
        return str('%s' % self.attachment_code)


class CBWPNote(models.Model):
    note_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='Note Number')
    title = models.CharField(max_length=100, verbose_name='CBWP Note Title')
    cbwp = models.ForeignKey(CBWP, on_delete=models.CASCADE, verbose_name='CBWP ID', default=1)
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "CBWP Notes"
        db_table = 'cbwp_note'
        app_label = 'j_cb'
        ordering = ['title']
        unique_together = ['cbwp', 'title', ]

    def __str__(self):
        return str('%s' % self.title)


# class CBWPChangesMatrixDefinition(models.Model):
#     change_code = models.CharField(unique=True, max_length=1, verbose_name='Change Code')
#     change_title = models.CharField(unique=True, max_length=15, verbose_name='Change Title')
#
#     class Meta:
#         managed = True
#         verbose_name_plural = "CBWP Changes Matrix Definition"
#         db_table = 'cbwp_changes_matrix_definition'
#         app_label = 'j_cb'
#         ordering = ['change_code']
#
#     def __str__(self):
#         return str('%s' % self.change_code)


class CBWPChanges(models.Model):
    change_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
                                    verbose_name='Change Number')
    title = models.CharField(max_length=100, verbose_name='CBWP Note Title')
    cbwp = models.ForeignKey(CBWP, on_delete=models.CASCADE, verbose_name='CBWP ID', default=1)
    change_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                        verbose_name='Change Amount', )
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "CBWP Changes"
        db_table = 'cbwp_changes'
        app_label = 'j_cb'
        ordering = ['title']
        unique_together = ['cbwp', 'title', ]

    def __str__(self):
        return str('%s' % self.title)