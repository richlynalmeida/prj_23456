from django.contrib import admin
from . import models
from .models import DatabaseViewsCEBTrends


@admin.register(DatabaseViewsCEBTrends)
class DatabaseViewsCEBTrendsAdmin(admin.ModelAdmin):
    list_display = ["tm_oeb_id", "oeb_code", "oeb_title", "oeb_hours", "oeb_costs", "tm_ceb_trends_count",
                    "ceb_trend_hours_agg", "ceb_trend_costs_agg", "ceb_hours", "ceb_costs", ]

    def has_add_permission(self, request, obj=None):
        return False