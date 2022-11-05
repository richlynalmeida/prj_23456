from django.db import models
from j_cb.models import CBWP
from djmoney.models.fields import MoneyField


class CBWPActuals(models.Model):
    cbwp = models.ForeignKey(CBWP, on_delete=models.CASCADE, verbose_name='CBWP ID')
    calendar_date = models.DateTimeField(verbose_name='Calendar Date')
    forecast_actual_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                verbose_name='Forecasted Actuals Hours on Calendar Date',
                                                default=0)
    # forecast_actual_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                             verbose_name='Forecasted Actuals Costs on Calendar Date',
    #                                             default=0)
    forecast_actual_costs = MoneyField(max_digits=18, decimal_places=2, blank=True, null=True,
                                       verbose_name='Forecasted Actuals Costs on Calendar Date',
                                       default_currency='CAD')
    incurred_actual_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                verbose_name='Incurred Actuals Hours on Calendar Date',
                                                default=0)
    # incurred_actual_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                             verbose_name='Incurred Actuals Costs on Calendar Date',
    #                                             default=0)
    incurred_actual_costs = MoneyField(max_digits=18, decimal_places=2, blank=True, null=True,
                                       verbose_name='Incurred Actuals Costs on Calendar Date',
                                       default_currency='CAD')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        unique_together = (('cbwp', 'calendar_date'),)
        verbose_name_plural = "CBWP Actuals"
        db_table = 'cbwp_actuals'
        app_label = 'l_actuals'
        ordering = ['cbwp', 'calendar_date']

    def __bytes__(self):
        return bytes('%s %s' % (self.calendar_date, self.cbwp))
