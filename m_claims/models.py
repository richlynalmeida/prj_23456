from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from f_contracts.models import ContractClauses
from j_cb.models import CBWP
from djmoney.models.fields import MoneyField
from djmoney.money import Money


class ClaimType(models.Model):
    claim_type_code = models.CharField(unique=True, max_length=5, verbose_name='Claim Type Code')
    claim_type_title = models.CharField(unique=True, max_length=55, verbose_name='Claim Type Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Claims - Types"
        db_table = 'claim_type'
        app_label = 'm_claims'
        ordering = ['claim_type_code']

    # def __str__(self):
    #     return str('%s' % self.claim_type_code)
    def __str__(self):
        return f"{self.claim_type_code} - {self.claim_type_title}"


class ClaimRoute(models.Model):
    claim_route_code = models.CharField(unique=True, max_length=5, verbose_name='Claim Type Code')
    claim_route_title = models.CharField(unique=True, max_length=55, verbose_name='Claim Type Title')

    class Meta:
        managed = True
        verbose_name_plural = "Claims - Route"
        db_table = 'claim_route'
        app_label = 'm_claims'
        ordering = ['claim_route_code']

    # def __str__(self):
    #     return str('%s' % self.claim_route_code)
    def __str__(self):
        return f"{self.claim_route_code} - {self.claim_route_title}"


class CBWPClaimDetail(models.Model):
    cbwp = models.ForeignKey(CBWP, verbose_name='CBWP ID', on_delete=models.CASCADE)
    claim_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                       verbose_name='Claim Number')
    claim_initiation_date = models.DateTimeField(verbose_name='Claim Initiation Date', )
    claim_type = models.ForeignKey(ClaimType, on_delete=models.CASCADE, unique=False,
                                   verbose_name='Claim Type ID', default=1)
    claim_title = models.CharField(unique=True, max_length=55, verbose_name='Claim Title')
    claim_summary = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Claim Summary')
    claim_route = models.ForeignKey(ClaimRoute, on_delete=models.CASCADE, unique=False,
                                    verbose_name='Claim Route ID', default=1)
    cbwp_hours_change_sought = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                  verbose_name='CBWP Hours Change Sought',
                                                  default=0)
    cbwp_hours_change_approved = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                  verbose_name='CBWP Hours Change Approved',
                                                  default=0)
    cbwp_costs_change_sought = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                  verbose_name='CBWP Costs Change Sought',
                                                  default=0)
    cbwp_costs_change_approved = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                  verbose_name='CBWP Costs Change Approved',
                                                  default=0)
    cbwp_daily_extension_sought = models.IntegerField(blank=True, null=True,
                                                      verbose_name='CBWP Daily Extension Sought')
    cbwp_daily_extension_approved = models.IntegerField(blank=True, null=True,
                                                        verbose_name='CBWP Daily Extension Approved')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "CBWP Claims"
        db_table = 'cbwp_claim'
        app_label = 'm_claims'
        unique_together = ['cbwp', 'claim_number']


class CBWPClaimDetailContractClauseReferences(models.Model):
    cbwp_claim = models.ForeignKey(CBWPClaimDetail, unique=False, on_delete=models.CASCADE,
                                   verbose_name='CBWP Claim Detail ID', default=1)
    contract_clause = models.ForeignKey(ContractClauses, unique=False, on_delete=models.CASCADE,
                                        verbose_name='Contract Clause ID', default=1)
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "CBWP Claims With Contract Clauses"
        db_table = 'cbwp_claim_clause'
        app_label = 'm_claims'
        unique_together = ['cbwp_claim', 'contract_clause']