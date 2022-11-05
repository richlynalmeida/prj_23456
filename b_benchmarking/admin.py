from django.contrib import admin
from . import models
from django.forms.widgets import TextInput
from f_contracts.models import Contract
from django import forms

admin.site.register(models.Projects)
admin.site.register(models.ProjectPhases)
admin.site.register(models.WBSLocationsForProjectPhases)
admin.site.register(models.CommodityWeightedUnitPriceAverages)
admin.site.register(models.CommodityWeightedUnitPriceAverageDetails)
admin.site.register(models.ProjectDataRepositoryCostItems)
admin.site.register(models.ProjectDataRepositoryCostItemDetails)