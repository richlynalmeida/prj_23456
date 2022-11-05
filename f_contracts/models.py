from django.db import models
from a_hr.models import Company, StakeholderRoles
from b_wbs.models import Discipline
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from g_measures.models import UOM


class ContractType(models.Model):
    contract_type_code = models.CharField(unique=True, max_length=2, verbose_name='Contract Type Code')
    contract_type_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                           verbose_name='Contract Type Title')

    class Meta:
        managed = True
        verbose_name_plural = "Contract Types"
        db_table = 'contract_type'
        app_label = 'f_contracts'
        ordering = ['contract_type_code']

    # def __str__(self):
    #     return str('%s' % self.contract_type_code)
    def __str__(self):
        return f"{self.contract_type_code} - {self.contract_type_title}"


class ContractPricingStyle(models.Model):
    contract_pricing_style_code = models.CharField(unique=True, max_length=5,
                                                   verbose_name='Contract Pricing Style Code')
    contract_pricing_style_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                                    verbose_name='Contract Pricing Style Title')

    class Meta:
        managed = True
        verbose_name_plural = "Contract Pricing Styles"
        db_table = 'contract_pricing_style'
        app_label = 'f_contracts'
        ordering = ['contract_pricing_style_code']

    # def __str__(self):
    #     return str('%s' % self.contract_pricing_style_code)
    def __str__(self):
        return f"{self.contract_pricing_style_code} - {self.contract_pricing_style_title}"


class Contract(models.Model):
    contract_type = models.ForeignKey(ContractType, on_delete=models.CASCADE,
                                      verbose_name='Contract Type Code')
    contract_pricing_style = models.ForeignKey(ContractPricingStyle, on_delete=models.CASCADE,
                                               verbose_name='Contract Pricing Style Code')
    parent_contract = models.ForeignKey("f_contracts.Contract", on_delete=models.CASCADE,
                                        verbose_name='Parent Contract Code', null=True, blank=True, default=1)
    contract_code = models.CharField(unique=True, max_length=10, verbose_name='Contract Code')
    contract_title = models.CharField(unique=True, max_length=100, blank=True, null=True, verbose_name='Contract Title')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Discipline ID')
    contract_tender_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                verbose_name='Contract Tender Costs',
                                                default=0)
    contract_award_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                               verbose_name='Contract Award Costs',
                                               default=0)
    start_date = models.DateTimeField(blank=True, null=True, verbose_name='Contract Start Date')
    finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Contract Finish Date')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Contract Code Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Contracts"
        db_table = 'contract'
        app_label = 'f_contracts'
        ordering = ['contract_code']

    # def __str__(self):
    #     return str('%s' % self.contract_code)
    def __str__(self):
        return f"{self.contract_code} - {self.contract_title}"


class ContractAudit(models.Model):
    contract_id = models.IntegerField(verbose_name='Contract ID')
    contract_code = models.CharField(max_length=10, verbose_name='Contract Code')
    contract_title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Contract Title')
    discipline_id = models.IntegerField(verbose_name='Discipline ID')
    contract_type_id = models.IntegerField(verbose_name='Contract Type ID')
    contract_pricing_style_id = models.IntegerField(verbose_name='Contract Pricing Style ID')
    parent_contract_id = models.IntegerField(verbose_name='Parent Contract ID')
    contract_tender_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                verbose_name='Contract Tender Costs')
    contract_award_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                               verbose_name='Contract Award Costs')
    start_date = models.DateTimeField(unique=False, verbose_name='Start Date')
    finish_date = models.DateTimeField(unique=False, verbose_name='Finish Date')
    comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='Comments')
    dml_action = models.CharField(max_length=2000, blank=True, null=True, verbose_name='DML Action')
    modified_by = models.CharField(unique=False, max_length=55, verbose_name='Modified By')
    modified_date = models.DateTimeField(unique=False, verbose_name='Modified Date')

    class Meta:
        managed = True
        verbose_name_plural = "Contract Details - Audit"
        db_table = 'contract_audit'
        app_label = 'f_contracts'
        ordering = ['contract_code']

    def __str__(self):
        return str('%s' % self.contract_code)


class ContractSecondaryInfo(models.Model):
    # PRIME_CONTRACTOR = 'PC'
    # GENERAL_CONTRACTOR = 'GC'
    # SUBCONTRACTOR = 'SC'
    # SUPPLIER = 'SL'
    # VENDOR_ROLE = [
    #     (PRIME_CONTRACTOR, 'PC'),
    #     (GENERAL_CONTRACTOR, 'GC'),
    #     (SUBCONTRACTOR, 'SC'),
    #     (SUPPLIER, 'SL'),
    # ]
    contract = models.ForeignKey(Contract, verbose_name='Contract ID', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name='Company ID', on_delete=models.CASCADE)
    stakeholder_role = models.ForeignKey(StakeholderRoles, verbose_name='Stakeholder Role ID', on_delete=models.CASCADE)
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Contract Vendor Information"
        db_table = 'contract_secondary_info'
        app_label = 'f_contracts'
        unique_together = ['contract', 'company', 'stakeholder_role']

    def __str__(self):
        return bytes('%s %s %s' % (self.contract, self.company, self.stakeholder_role))


class ContractClauses(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE,
                                 verbose_name='Contract ID', unique=False, default=1)
    contract_clause_number = models.CharField(unique=True, max_length=15, verbose_name='Contract Clause Number')
    contract_clause_title = models.CharField(unique=True, max_length=55, verbose_name='Contract Clause Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Contract Clauses"
        db_table = 'contract_clause'
        app_label = 'f_contracts'
        ordering = ['contract_clause_number']

    def __str__(self):
        return str('%s' % self.contract_clause_number)


class TrendTypes(models.Model):
    trend_type_code = models.CharField(unique=True, max_length=5,
                                       verbose_name='Trend Type Code')
    trend_type_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                        verbose_name='Trend Type Title')
    scope_related_check = models.IntegerField(default=0, verbose_name='Scope Related Check')

    # 0 - Non-Scope Related; 1 - Scope Related

    class Meta:
        managed = True
        verbose_name_plural = "Trend Types"
        db_table = 'tm_trend_type'
        app_label = 'f_contracts'
        ordering = ['trend_type_code']

    # def __str__(self):
    #     return str('%s' % self.contract_pricing_style_code)
    def __str__(self):
        return f"{self.trend_type_code} - {self.trend_type_title}"
