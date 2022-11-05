from django.db import models
from j_cb.models import CBWP
from djmoney.models.fields import MoneyField
from djmoney.money import Money


class DatabaseViewsCEBTrends(models.Model):
    tm_oeb_id = models.IntegerField(primary_key=True)
    oeb_code = models.CharField(max_length=100, verbose_name='OEB Code')
    oeb_title = models.CharField(max_length=100, verbose_name='OEB Title')
    oeb_hours = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='OEB Hours')
    oeb_costs = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='OEB Costs')
    tm_ceb_trends_count = models.IntegerField(verbose_name='CEB Trend Count')
    ceb_trend_hours_agg = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='CEB Trend Hours Agg')
    ceb_trend_costs_agg = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='CEB Trend Costs Agg')
    ceb_hours = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='CEB Hours')
    ceb_costs = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='CEB Costs')

    class Meta:
        managed = False
        db_table = "vw_tm_oeb_cebtrends_agg_02_ceb"
        verbose_name_plural = "CEB Trends Aggregate"
        app_label = 'v_viewsdbo'
        ordering = ['oeb_code']
