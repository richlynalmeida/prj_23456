from django.db import models
from j_cb.models import CBWP
from djmoney.models.fields import MoneyField


class CBWPAccountsReceivable(models.Model):
    cbwp = models.ForeignKey(CBWP, on_delete=models.CASCADE, verbose_name='CBWP ID')
    calendar_date = models.DateTimeField(verbose_name='Calendar Date')
    # ar_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                verbose_name='Accounts Receivable Costs on Calendar Date', default=0)
    ar_costs = MoneyField(max_digits=18, decimal_places=2, blank=True, null=True,
                          verbose_name='Accounts Receivable Costs on Calendar Date',
                          default_currency='CAD')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        unique_together = (('cbwp', 'calendar_date'),)
        verbose_name_plural = "CBWP Accounts Receivable"
        db_table = 'cbwp_accounts_receivable'
        app_label = 'f_finance'
        ordering = ['cbwp', 'calendar_date']

    def __bytes__(self):
        return bytes('%s %s' % (self.calendar_date, self.cbwp))


class CBWPAccountsPayable(models.Model):
    cbwp = models.ForeignKey(CBWP, on_delete=models.CASCADE, verbose_name='CBWP ID')
    calendar_date = models.DateTimeField(verbose_name='Calendar Date')
    # ap_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                verbose_name='Accounts Payable Costs on Calendar Date', default=0)
    ap_costs = MoneyField(max_digits=18, decimal_places=2, blank=True, null=True,
                          verbose_name='Accounts Payable Costs on Calendar Date',
                          default_currency='CAD')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        unique_together = (('cbwp', 'calendar_date'),)
        verbose_name_plural = "CBWP Accounts Payable"
        db_table = 'cbwp_accounts_payable'
        app_label = 'f_finance'
        ordering = ['cbwp', 'calendar_date']

    def __bytes__(self):
        return bytes('%s %s' % (self.calendar_date, self.cbwp))
