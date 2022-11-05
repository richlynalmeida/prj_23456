from django.db import models
from a_hr.models import Personnel, RaciMatrixDefinition
from b_wbs.models import CostType, Department, Discipline, WBSLocation, FacilitySystemDetail, EBWPType, EBWPStatus
from e_commodities.models import CommodityType, Commodity
from f_contracts.models import Contract
from f_contracts.models import TrendTypes
from g_measures.models import UOM
from h_schedules.models import EBSchedule
from django.core.validators import MinValueValidator, MaxValueValidator
from djmoney.models.fields import MoneyField
from djmoney.money import Money


class OriginalEstimateBudget(models.Model):
    oeb_code = models.CharField(unique=True, max_length=55, verbose_name='OEB Code')
    oeb_title = models.CharField(unique=True, max_length=200, blank=True, null=True, verbose_name='OEB Title')
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE, verbose_name='OEB Cost Type ID',
                                  default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   verbose_name='OEB Department ID', default=1)
    oeb_comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='OEB Comments')
    # Quantification, Pricing, Hours and Costs
    oeb_qty = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='OEB Quantity')
    oeb_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='eb UOM ID', default=1)
    oeb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='OEB Hours', default=0)
    oeb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='OEB Costs')
    oeb_approval_check = models.IntegerField(default=0, verbose_name='Approval Check')

    class Meta:
        managed = True
        verbose_name_plural = "Original Estimate Budget"
        db_table = 'tm_oeb'
        app_label = 'i_eb'
        ordering = ['oeb_code']

    def __str__(self):
        return f"{self.oeb_code} - {self.oeb_title}"


class OEBRaciInformation(models.Model):
    tm_oeb = models.ForeignKey(OriginalEstimateBudget, on_delete=models.CASCADE, verbose_name='OEB ID',
                               default=1)
    personnel = models.ForeignKey(Personnel, verbose_name='Personnel ID', on_delete=models.CASCADE, default=1)
    raci = models.ForeignKey(RaciMatrixDefinition, verbose_name='Raci ID', on_delete=models.CASCADE, default=1)
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Original Estimate Budget RACI Information"
        db_table = 'tm_oeb_raci_info'
        app_label = 'i_eb'
        unique_together = ['tm_oeb', 'personnel', 'raci']


class CurrentEstimateBudgetTrends(models.Model):
    tm_oeb = models.ForeignKey(OriginalEstimateBudget, on_delete=models.CASCADE, verbose_name='OEB ID',
                               default=1)
    ceb_trend_type = models.ForeignKey(TrendTypes, on_delete=models.CASCADE, verbose_name='CEB Trend Type ID',
                                       default=1)
    ceb_trend_qty = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                        verbose_name='CEB Trend Quantity')
    ceb_trend_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CEB UOM ID', default=1)
    ceb_trend_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                          verbose_name='CEB Trend Hours', default=0)
    ceb_trend_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                          verbose_name='CEB Trend Costs')
    ceb_trend_code = models.CharField(unique=True, max_length=55, verbose_name='CEB Trend Code')
    ceb_trend_title = models.CharField(unique=True, max_length=200, blank=True, null=True,
                                       verbose_name='CEB Trend Title')
    ceb_trend_comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CEB Trend Comments')
    ceb_approval_check = models.IntegerField(default=0, verbose_name='Approval Check')

    class Meta:
        managed = True
        verbose_name_plural = "Current Estimate Budget Trends"
        db_table = 'tm_ceb_trends'
        app_label = 'j_cb'
        ordering = ['ceb_trend_code']

    def __str__(self):
        return f"{self.ceb_trend_code} - {self.ceb_trend_title}"


class CurrentEstimateBudget(models.Model):
    ceb_code = models.CharField(unique=True, max_length=55, verbose_name='CEB Code')
    ceb_title = models.CharField(unique=True, max_length=200, blank=True, null=True, verbose_name='CEB Title')
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE, verbose_name='CEB Cost Type ID',
                                  default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   verbose_name='CEB Department ID', default=1)
    ceb_comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CEB Comments')
    # Quantification, Pricing, Hours and Costs
    ceb_qty = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='CEB Quantity')
    ceb_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CEB UOM ID', default=1)
    ceb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CEB Hours', default=0)
    ceb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CEB Costs')
    ceb_approval_check = models.IntegerField(default=0, verbose_name='Approval Check')
    oeb_ceb_trend_import_check = models.IntegerField(default=0, verbose_name='Import from OEB and CEB Trend Check')

    class Meta:
        managed = True
        verbose_name_plural = "Current Estimate Budget"
        db_table = 'tm_ceb'
        app_label = 'i_eb'
        ordering = ['ceb_code']

    def __str__(self):
        return f"{self.ceb_code} - {self.ceb_title}"


class EBWP(models.Model):
    ebwp_code = models.CharField(unique=True, max_length=55, verbose_name='EBWP Code')
    ebwp_title = models.CharField(unique=True, max_length=200, blank=True, null=True, verbose_name='EBWP Title')
    ebwp_status = models.ForeignKey(EBWPStatus, on_delete=models.CASCADE, verbose_name='EBWP Status ID',
                                    default=1)
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE, verbose_name='EBWP Cost Type ID',
                                  default=1)
    ebwp_type = models.ForeignKey(EBWPType, on_delete=models.CASCADE, verbose_name='EBWP Type ID',
                                  default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   verbose_name='EBWP Department ID', default=1)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE,
                                   verbose_name='EBWP Discipline ID', default=1)
    wbs_location = models.ForeignKey(WBSLocation, verbose_name='WBS Location ID', on_delete=models.CASCADE,
                                     default=1)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE,
                                 verbose_name='EBWP Contract ID', default=1)
    commodity_type = models.ForeignKey(CommodityType, on_delete=models.CASCADE,
                                       verbose_name='EBWP Commodity Type ID', default=1)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE,
                                  verbose_name='EBWP Commodity ID', default=1)
    facility_system_detail = models.ForeignKey(FacilitySystemDetail, on_delete=models.CASCADE,
                                               verbose_name='EBWP Facility System Detail ID', default=1)
    eb_schedule = models.ForeignKey(EBSchedule, on_delete=models.CASCADE,
                                    verbose_name='EBWP Schedule Activity Code', default=1)
    ebwp_discretionary_start_date = models.DateTimeField(blank=True, null=True,
                                                         verbose_name='EBWP Discretionary Start Date')
    ebwp_discretionary_finish_date = models.DateTimeField(blank=True, null=True,
                                                          verbose_name='EBWP Discretionary Finish Date')
    ebwp_sibling = models.ForeignKey('i_eb.EBWP', on_delete=models.CASCADE,
                                     verbose_name='EBWP Sibling ID', null=True, blank=True, default=1)
    # General comments for the EBWP
    ebwp_comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='EBWP Comments')
    ebwp_primary_contact = models.CharField(unique=False, max_length=100, blank=True, null=True,
                                            verbose_name='EBWP Primary Contact or Owner')
    ebwp_secondary_contact = models.CharField(unique=False, max_length=100, blank=True, null=True,
                                              verbose_name='EBWP Secondary Contact')
    # Quantification, Pricing, Hours and Costs
    quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='EBWP Quantity')
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CBWP UOM ID', default=1)
    ebwp_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                     verbose_name='EBWP Hours', default=0)
    # The original budget of the Work Package - aka BAC (Budget At Completion), Control Budget (CB)
    # ebwp_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                  verbose_name='EBWP Costs')
    ebwp_costs = MoneyField(max_digits=18, decimal_places=2, blank=True, null=True,
                            verbose_name='EBWP Costs', default_currency='CAD', default=0)

    class Meta:
        managed = True
        verbose_name_plural = "EBWP Details"
        db_table = 'ebwp'
        app_label = 'i_eb'
        ordering = ['ebwp_code']

    # def __str__(self):
    #     return str('%s' % self.ebwp_code)
    def __str__(self):
        return f"{self.ebwp_code} - {self.ebwp_title}"


class EBWPAudit(models.Model):
    ebwp_id = models.IntegerField(verbose_name='EBWP ID')
    ebwp_code = models.CharField(max_length=55, verbose_name='EBWP Code')
    ebwp_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='EBWP Title')
    ebwp_status_id = models.IntegerField(verbose_name='EB Status ID')
    cost_type_id = models.IntegerField(verbose_name='Cost Type ID')
    ebwp_type_id = models.IntegerField(verbose_name='EB Type ID')
    department_id = models.IntegerField(verbose_name='Department ID')
    discipline_id = models.IntegerField(verbose_name='Discipline ID')
    wbs_location_id = models.IntegerField(verbose_name='WBS Location ID')
    contract_id = models.IntegerField(verbose_name='EBWP Contract ID')
    commodity_type_id = models.IntegerField(verbose_name='EBWP Commodity Type ID')
    commodity_id = models.IntegerField(verbose_name='EBWP Commodity ID')
    facility_system_detail_id = models.IntegerField(verbose_name='EBWP Facility System Detail ID')
    eb_schedule_id = models.IntegerField(verbose_name='EB Schedule ID')
    ebwp_discretionary_start_date = models.DateTimeField(blank=True, null=True,
                                                         verbose_name='EBWP Discretionary Start Date')
    ebwp_discretionary_finish_date = models.DateTimeField(blank=True, null=True,
                                                          verbose_name='EBWP Discretionary Finish Date')
    ebwp_sibling_id = models.IntegerField(verbose_name='EB Sibling ID', blank=True, null=True)
    ebwp_comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='EBWP Comments')
    ebwp_primary_contact = models.CharField(max_length=2000, blank=True, null=True,
                                            verbose_name='EBWP Primary Contact or Owner')
    ebwp_secondary_contact = models.CharField(max_length=2000, blank=True, null=True,
                                              verbose_name='EBWP Secondary Contact or Owner')

    quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='EBWP Quantity')
    uom_id = models.IntegerField(verbose_name='EBWP UOM ID')
    ebwp_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                     verbose_name='EBWP Hours')
    ebwp_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                     verbose_name='EBWP Costs')
    dml_action = models.CharField(max_length=2000, blank=True, null=True, verbose_name='DML Action')
    modified_by = models.CharField(unique=False, max_length=55, verbose_name='Modified By')
    modified_date = models.DateTimeField(unique=False, verbose_name='Modified Date')

    class Meta:
        managed = True
        verbose_name_plural = "EBWP Details - Audit"
        db_table = 'ebwp_audit'
        app_label = 'i_eb'
        ordering = ['ebwp_code']

    def __str__(self):
        return str('%s' % self.ebwp_code)


class EBWPRaciInformation(models.Model):
    ebwp = models.ForeignKey(EBWP, verbose_name='EBWP ID', on_delete=models.CASCADE)
    personnel = models.ForeignKey(Personnel, verbose_name='Personnel ID', on_delete=models.CASCADE)
    raci = models.ForeignKey(RaciMatrixDefinition, verbose_name='Raci ID', on_delete=models.CASCADE)
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "EBWP RACI Information"
        db_table = 'ebwp_raci_info'
        app_label = 'i_eb'
        unique_together = ['ebwp', 'personnel', 'raci']


class EBWPNote(models.Model):
    note_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='Note Number')
    title = models.CharField(max_length=100, verbose_name='EBWP Note Title')
    ebwp = models.ForeignKey(EBWP, on_delete=models.CASCADE, verbose_name='EBWP ID', default=1)
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "EBWP Notes"
        db_table = 'ebwp_note'
        app_label = 'i_eb'
        ordering = ['title']

    def __str__(self):
        return str('%s' % self.title)


class EBWPCostDetails(models.Model):
    item_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
                                  unique=False, verbose_name='Item Number')
    item_title = models.CharField(unique=False, max_length=55, verbose_name='Item Title')
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE, verbose_name='EBWP Detail Cost Type ID',
                                  unique=False)
    item_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                     verbose_name='Item Costs', )
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')
    ebwp = models.ForeignKey(EBWP, on_delete=models.CASCADE, verbose_name='EBWP ID', default=1)

    class Meta:
        managed = True
        verbose_name_plural = "EBWP Cost Details"
        db_table = 'ebwp_cost_detail'
        app_label = 'i_eb'
        ordering = ['item_title']
        unique_together = ['item_title', 'cost_type', 'ebwp']

    def __str__(self):
        return str('%s' % self.item_title)


class EBWPAttachment(models.Model):
    ebwp = models.ForeignKey(EBWP, on_delete=models.CASCADE, verbose_name='EBWP ID', default=1)
    attachment_code = models.CharField(unique=True, max_length=100, verbose_name='Attachment Code')
    attachment_title = models.CharField(max_length=100, verbose_name='Attachment Title')
    revision_number = models.CharField(max_length=3, blank=True, null=True, verbose_name='Revision No')
    revision_status = models.CharField(max_length=55, blank=True, null=True, verbose_name='Revision Status')
    release_date = models.DateTimeField(blank=True, null=True, verbose_name='Release Date')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='EBWP Attachment Comments')
    ebwp_attachment = models.FileField(blank=True, null=True, upload_to='EBWPAttachments/',
                                       verbose_name='EBWP Attachments')
    ebwp_url = models.URLField(blank=True, null=True, max_length=250, verbose_name='EBWP URL')

    class Meta:
        managed = True
        verbose_name_plural = "EBWP Attachments"
        db_table = 'ebwp_attachment'
        app_label = 'i_eb'
        ordering = ['attachment_code']

    def __str__(self):
        return str('%s' % self.attachment_code)
