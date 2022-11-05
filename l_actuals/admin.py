from django import forms
from django.contrib import admin
# from django.contrib.admin import forms
# from djmoney import forms
from django.db import models
from l_actuals.models import CBWPActuals
from django.forms.widgets import TextInput


@admin.register(CBWPActuals)
class CBWPActualsAdmin(admin.ModelAdmin):
    list_display = ['cbwp', 'calendar_date', 'forecast_actual_costs', 'incurred_actual_costs', 'id', ]
    list_filter = ['cbwp', 'calendar_date', 'forecast_actual_costs', 'incurred_actual_costs', 'id', ]

    # formfield_overrides = {
    #     models.DecimalField: {
    #         'widget': forms.TextInput(attrs={'style': 'text-align:right;', }),
    #     },
    # }
