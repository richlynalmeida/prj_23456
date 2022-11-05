from django.db import models
from b_wbs.models import Discipline, EBWPType, CBWPType


class EBSchedule(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Discipline Code')
    ebwp_type = models.ForeignKey(EBWPType, on_delete=models.CASCADE, verbose_name='EBWP Type Code')
    eb_schedule_code = models.CharField(unique=True, max_length=55, verbose_name='EB Schedule Code')
    eb_schedule_title = models.CharField(max_length=2000, blank=True, null=True, verbose_name='EB Schedule Title')
    early_start_date = models.DateTimeField(blank=True, null=True, verbose_name='EB Early Start Date')
    early_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='EB Early Finish Date')
    early_start_to_early_finish_duration = models.IntegerField(blank=True, null=True,
                                                               verbose_name='EB Early Start to Early Finish Duration')
    late_start_date = models.DateTimeField(blank=True, null=True, verbose_name='EB Late Start Date')
    late_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='EB Late Finish Date')
    late_start_to_late_finish_duration = models.IntegerField(blank=True, null=True,
                                                             verbose_name='EB Late Start to Late Finish Duration')
    critical_path_check = models.IntegerField(default=0, verbose_name='EB Critical Path Check')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='EB Comments')

    class Meta:
        managed = True
        verbose_name_plural = "EB aka L03 Schedule"
        db_table = 'eb_schedule'
        app_label = 'h_schedules'
        ordering = ['eb_schedule_code']

    # def __str__(self):
    #     return str('%s' % self.eb_schedule_code)
    def __str__(self):
        return f"{self.eb_schedule_code} - {self.eb_schedule_title}"


class CBSchedule(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Discipline Code')
    cbwp_type = models.ForeignKey(CBWPType, on_delete=models.CASCADE, verbose_name='CBWP Type Code')
    eb_schedule = models.ForeignKey(EBSchedule, on_delete=models.CASCADE,
                                    verbose_name='EB Schedule Code')
    cb_schedule_code = models.CharField(unique=True, max_length=55, verbose_name='CB Schedule Code')
    cb_schedule_title = models.CharField(max_length=2000, blank=True, null=True, verbose_name='CB Schedule Title')
    early_start_date = models.DateTimeField(blank=True, null=True, verbose_name='CB Early Start Date')
    early_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='CB Early Finish Date')
    early_start_to_early_finish_duration = models.IntegerField(blank=True, null=True,
                                                               verbose_name='CB Early Start to Early Finish Duration')
    late_start_date = models.DateTimeField(blank=True, null=True, verbose_name='CB Late Start Date')
    late_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='CB Late Finish Date')
    late_start_to_late_finish_duration = models.IntegerField(blank=True, null=True,
                                                             verbose_name='CB Late Start to Late Finish Duration')
    critical_path_check = models.IntegerField(default=0, verbose_name='CB Critical Path Check')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='CB Comments')

    class Meta:
        managed = True
        verbose_name_plural = "CB aka L04 Schedule"
        db_table = 'cb_schedule'
        app_label = 'h_schedules'
        ordering = ['cb_schedule_code']

    # def __str__(self):
    #     return str('%s' % self.cb_schedule_code)
    def __str__(self):
        return f"{self.cb_schedule_code} - {self.cb_schedule_title}"