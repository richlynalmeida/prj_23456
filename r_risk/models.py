from django.db import models
from a_hr.models import Personnel, Company, StakeholderRoles
from g_measures.models import Boolean
from j_cb.models import CBWP


class RiskProbability(models.Model):
    risk_probability_code = models.CharField(unique=True, max_length=5, verbose_name='Risk Probability Code', )
    risk_probability_title = models.CharField(unique=True, max_length=55, verbose_name='Risk Probability Title', )
    risk_probability_value = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,
                                                 verbose_name='Risk Probability Value')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Risk Probability"
        db_table = 'risk_probability'
        app_label = 'r_risk'
        ordering = ['risk_probability_code']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.risk_probability_code} - {self.risk_probability_title}"


class RiskTimeFrame(models.Model):
    risk_timeframe_code = models.CharField(unique=True, max_length=5, verbose_name='Risk TimeFrame Code', )
    risk_timeframe_title = models.CharField(unique=True, max_length=55, verbose_name='Risk TimeFrame Title', )
    risk_timeframe_value = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,
                                               verbose_name='Risk TimeFrame Value')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Risk TimeFrame"
        db_table = 'risk_timeframe'
        app_label = 'r_risk'
        ordering = ['risk_timeframe_code']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.risk_timeframe_code} - {self.risk_timeframe_title}"


class RiskCategory(models.Model):
    risk_category_code = models.CharField(unique=True, max_length=5, verbose_name='Risk Category Code', )
    risk_category_title = models.CharField(unique=True, max_length=55, verbose_name='Risk Category Title', )
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Risk Category"
        db_table = 'risk_category'
        app_label = 'r_risk'
        ordering = ['risk_category_code']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.risk_category_code} - {self.risk_category_title}"


class RiskSeverity(models.Model):
    risk_severity_code = models.CharField(unique=True, max_length=5, verbose_name='Risk Severity Code', )
    risk_severity_title = models.CharField(unique=True, max_length=55, verbose_name='Risk Severity Title', )
    risk_severity_value = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,
                                              verbose_name='Risk Severity Value')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Risk Severity"
        db_table = 'risk_severity'
        app_label = 'r_risk'
        ordering = ['risk_severity_code']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.risk_severity_code} - {self.risk_severity_title}"


class RiskUnderlyingAssumption(models.Model):
    risk_underlying_assumption_code = models.CharField(unique=True, max_length=5,
                                                       verbose_name='Risk Underlying Assumption Code', )
    risk_underlying_assumption_title = models.CharField(unique=True, max_length=55,
                                                        verbose_name='Risk Underlying Assumption Title', )
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Risk Underlying Assumption"
        db_table = 'risk_underlying_assumption'
        app_label = 'r_risk'
        ordering = ['risk_underlying_assumption_code']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.risk_underlying_assumption_code} - {self.risk_underlying_assumption_title}"


class RiskMonitoringMetric(models.Model):
    risk_monitoring_metric_code = models.CharField(unique=True, max_length=5,
                                                   verbose_name='Risk Monitoring Metric Code', )
    risk_monitoring_metric_title = models.CharField(unique=True, max_length=55,
                                                    verbose_name='Risk Monitoring Metric Title', )
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Risk Monitoring Metric"
        db_table = 'risk_monitoring_metric'
        app_label = 'r_risk'
        ordering = ['risk_monitoring_metric_code']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.risk_monitoring_metric_code} - {self.risk_monitoring_metric_title}"


class Risks(models.Model):
    risk_title = models.CharField(unique=True, max_length=55, verbose_name='Risk Title', )
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')
    stakeholder_role = models.ForeignKey(StakeholderRoles, on_delete=models.CASCADE,
                                         verbose_name='Stakeholder Role ID')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Company ID')
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE,
                                  verbose_name='Personnel ID')
    risk_underlying_assumption = models.ForeignKey(RiskUnderlyingAssumption, on_delete=models.CASCADE,
                                                   verbose_name='Risk Underlying Assumption ID')
    risk_category = models.ForeignKey(RiskCategory, on_delete=models.CASCADE,
                                      verbose_name='Risk Category ID')
    risk_severity = models.ForeignKey(RiskSeverity, on_delete=models.CASCADE,
                                      verbose_name='Risk Severity ID')
    risk_probability = models.ForeignKey(RiskProbability, on_delete=models.CASCADE,
                                         verbose_name='Risk Probability ID')
    risk_timeframe = models.ForeignKey(RiskTimeFrame, on_delete=models.CASCADE,
                                       verbose_name='Risk TimeFrame ID')
    risk_monitoring_metric = models.ForeignKey(RiskMonitoringMetric, on_delete=models.CASCADE,
                                               verbose_name='Risk Monitoring Metric ID')
    cbwp = models.ForeignKey(CBWP, on_delete=models.CASCADE, verbose_name='CBWP ID', default=1)
    cost_or_schedule = models.CharField(unique=False, max_length=8, verbose_name='cost or Schedule', default='Cost')

    # class CostOrSchedule(models.TextChoices):
    #     a = 'C', "Cost"
    #     b = 'S', "Schedule"
    #
    # cost_or_schedule = models.CharField(
    #     max_length=1,
    #     choices=CostOrSchedule.choices,
    #     default=CostOrSchedule.a
    # )

    class Meta:
        managed = True
        verbose_name_plural = "Risks"
        db_table = 'risk'
        app_label = 'r_risk'
        ordering = ['risk_category']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.risk_title}"


class RiskMitigationStrategyType(models.Model):
    risk_mitigation_strategy_type_code = models.CharField(unique=True, max_length=5,
                                                          verbose_name='Risk Mitigation Strategy Type Code', )
    risk_mitigation_strategy_type_title = models.CharField(unique=True, max_length=55,
                                                           verbose_name='Risk Mitigation Strategy Type Title', )
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Risk Mitigation Strategy Type"
        db_table = 'risk_mitigation_strategy_type'
        app_label = 'r_risk'
        ordering = ['risk_mitigation_strategy_type_code']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.risk_mitigation_strategy_type_code} - {self.risk_mitigation_strategy_type_title}"


class RiskMitigationStrategies(models.Model):
    rms_title = models.CharField(unique=True, max_length=55,
                                 verbose_name='Risk Mitigation Strategy Title', )
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')
    risk = models.ForeignKey(Risks, on_delete=models.CASCADE,
                             verbose_name='Risk ID')
    rms_type = models.ForeignKey(RiskMitigationStrategyType, on_delete=models.CASCADE,
                                 verbose_name='Risk Mitigation Strategy Type ID')
    rms_implementation_date = models.DateTimeField(blank=True, null=True,
                                                   verbose_name='Risk Mitigation Strategy Implementation Date')
    rms_implementation_estimated_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                             verbose_name='Risk Mitigation Strategy Implementation '
                                                                          'Estimated Costs',
                                                             help_text='Estimated cost of the risk mitigation '
                                                                       'strategy implementation')
    rms_implementation_actual_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                          verbose_name='Risk Mitigation Strategy Implementation '
                                                                       'Actual Costs',
                                                          help_text='Actual cost of the risk mitigation strategy '
                                                                    'implementation')
    rms_success_metric = models.CharField(max_length=2000, blank=True, null=True,
                                          verbose_name='Risk Mitigation Strategy Success Metric')
    rms_success_check = models.ForeignKey(Boolean, on_delete=models.CASCADE,
                                          verbose_name='Risk Mitigation Strategy Success Check')
    rms_success_check_date = models.DateTimeField(blank=True, null=True,
                                                  verbose_name='Risk Mitigation Strategy Success Check Date')
    rms_success_failure_comments = models.CharField(max_length=2000, blank=True, null=True,
                                                    verbose_name='Risk Mitigation Strategy Success or Failure Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Risk Mitigation Strategies"
        db_table = 'risk_mitigation_strategy'
        app_label = 'r_risk'
        ordering = ['rms_title']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.rms_title}"


class RiskContingencyPlan(models.Model):
    rcp_title = models.CharField(unique=True, max_length=55,
                                 verbose_name='Risk Contingency Plan', )
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')
    risk_mitigation_strategy = models.ForeignKey(RiskMitigationStrategies, on_delete=models.CASCADE,
                                                 verbose_name='Risk Mitigation Strategy ID')
    trigger = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Trigger',
                               help_text='Description of the condition which will trigger the execution of the '
                                         'risk contingency plan')
    rcp_implementation_date = models.DateTimeField(blank=True, null=True,
                                                   verbose_name='Risk Contingency Plan Implementation Date')
    rcp_implementation_estimated_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                             verbose_name='Risk Contingency Plan Implementation '
                                                                          'Estimated Costs',
                                                             help_text='Estimated cost of the Risk Contingency Plan '
                                                                       'implementation')
    rcp_implementation_actual_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                                          verbose_name='Risk Contingency Plan Implementation '
                                                                       'Actual Costs',
                                                          help_text='Actual cost of the Risk Contingency Plan '
                                                                    'implementation')
    rcp_success_check = models.ForeignKey(Boolean, on_delete=models.CASCADE,
                                          verbose_name='Risk Contingency Plan Success Check')
    rcp_success_check_date = models.DateTimeField(blank=True, null=True,
                                                  verbose_name='Risk Contingency Plan Success Check Date')
    rcp_success_failure_comments = models.CharField(max_length=2000, blank=True, null=True,
                                                    verbose_name='Risk Contingency Plan Success or Failure Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Risk Contingency Plan"
        db_table = 'risk_contingency_plan'
        app_label = 'r_risk'
        ordering = ['rcp_title']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.rcp_title}"
