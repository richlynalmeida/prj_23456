from django.contrib import admin
from . import models


admin.site.register(models.RiskProbability)
admin.site.register(models.RiskSeverity)
admin.site.register(models.RiskCategory)
admin.site.register(models.RiskTimeFrame)
admin.site.register(models.RiskUnderlyingAssumption)
admin.site.register(models.RiskMonitoringMetric)
admin.site.register(models.Risks)
admin.site.register(models.RiskMitigationStrategyType)
admin.site.register(models.RiskMitigationStrategies)
admin.site.register(models.RiskContingencyPlan)