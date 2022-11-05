from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Boolean(models.Model):
    boolean_code = models.CharField(unique=True, max_length=1, verbose_name='Boolean Code', default='0')
    boolean_title = models.CharField(unique=True, max_length=1, verbose_name='Boolean Title', default='F')

    class Meta:
        managed = True
        verbose_name_plural = 'Boolean'
        db_table = 'boolean'
        app_label = 'g_measures'
        ordering = ['boolean_code']

    # def __str__(self):
    #     return str('%s' % self.boolean_code)
    def __str__(self):
        return f"{self.boolean_code} - {self.boolean_title}"


class UOMSystem(models.Model):
    uom_system_code = models.CharField(unique=True, max_length=1, verbose_name='UOM System Code')
    uom_system_title = models.CharField(unique=True, max_length=55, verbose_name='UOM System Title')

    class Meta:
        managed = True
        verbose_name_plural = "Units of Measures System"
        db_table = 'uom_system'
        app_label = 'g_measures'
        ordering = ['uom_system_code']

    # def __str__(self):
    #     return str('%s' % self.uom_system_code)
    def __str__(self):
        return f"{self.uom_system_code} - {self.uom_system_title}"


class UOM(models.Model):
    uom_system = models.ForeignKey(UOMSystem, on_delete=models.CASCADE, verbose_name='UOM System ID')
    uom_code = models.CharField(max_length=3, verbose_name='UOM Code')
    uom_title = models.CharField(max_length=55, verbose_name='UOM Title')

    class Meta:
        managed = True
        verbose_name_plural = "Units of Measures"
        db_table = 'uom'
        app_label = 'g_measures'
        ordering = ['uom_code']
        unique_together = ['uom_system', 'uom_code']

    # def __str__(self):
    #     return str('%s' % self.uom_code)
    def __str__(self):
        return f"{self.uom_code} - {self.uom_title}"


class MilepostTemplate(models.Model):
    milepost_template_code = models.CharField(unique=True, max_length=10, verbose_name='Milepost Template Code')
    milepost_template_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                               verbose_name='Milepost Template Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Milepost Template"
        db_table = 'milepost_template'
        app_label = 'g_measures'
        ordering = ['milepost_template_code']

    # def __str__(self):
    #     return str('%s' % self.milepost_template_code)
    def __str__(self):
        return f"{self.milepost_template_code} - {self.milepost_template_title}"


class MilepostTemplateDetail(models.Model):
    milepost_template = models.ForeignKey(MilepostTemplate, on_delete=models.CASCADE,
                                          verbose_name='Milepost Template ID')
    step_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Step Number')
    short_desc = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Short Description')
    long_desc = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Long Description')
    step_budget = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                      verbose_name='Allocated Budget at this Step')
    step_cum_budget = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                          verbose_name='Cumulative Budget at this Step')
    xref_tags_col_name_p = models.CharField(max_length=12, blank=True, null=True,
                                            verbose_name='P Column Name X Ref', default='mp_01_date_p')
    xref_tags_col_name_e = models.CharField(max_length=12, blank=True, null=True,
                                            verbose_name='E Column Name X Ref', default='mp_01_date_e')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Milepost Template Details"
        db_table = 'milepost_template_detail'
        app_label = 'g_measures'
        ordering = [['milepost_template', 'step_no']]
        unique_together = [['milepost_template', 'step_no']]

    def __str__(self):
        return str(
            '%s %s %s %s' % (self.milepost_template, self.step_no, self.short_desc, self.step_budget))


# class Audit(models.Model):
#     table_name = models.CharField(max_length=50, verbose_name='Table Name')
#     user_name = models.CharField(max_length=50, verbose_name='User Name')
#     action_timestamp = models.DateTimeField(unique=False, verbose_name='Action Timestamp', blank=False,
#                                             null=False, auto_now_add=True)
#     action_choices = (
#         ('I', 'I'),
#         ('U', 'U'),
#         ('D', 'D'),
#     )
#     action = models.CharField(max_length=1, choices=action_choices, verbose_name='Action')
#     old_values = HStoreField()
#     new_values = HStoreField()
#     updated_cols = models.CharField(max_length=50, verbose_name='Updated Columns')
#     query = models.CharField(max_length=2000, verbose_name='Query')
#
#     class Meta:
#         managed = True
#         verbose_name_plural = "Audit"
#         db_table = 'audit'
#         app_label = 'g_measures'
