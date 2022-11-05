from django.db import models
from a_hr.models import Company, StakeholderRoles
from b_wbs.models import Discipline
from g_measures.models import UOMSystem, UOM
from e_commodities.models import CommodityTypeCameose, CommodityCameose, CommodityDetailCameose
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from django.core.validators import MinValueValidator, MaxValueValidator


class Projects(models.Model):
    project_code = models.CharField(unique=True, max_length=5, verbose_name='Project Code')
    project_title = models.CharField(max_length=55, blank=True, null=True, verbose_name='Project Title')
    client_name = models.CharField(max_length=55, blank=True, null=True, verbose_name='Client Name')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Project Comments')

    class Meta:
        # abstract = True
        managed = True
        verbose_name_plural = 'Projects'
        db_table = 'projects'
        # app_label = 'Benchmarking'
        app_label = 'b_benchmarking'
        ordering = ['project_code']

    def __str__(self):
        return str('%s' % self.project_code)


class ProjectPhases(models.Model):
    project_phase_code = models.CharField(unique=True, max_length=5, verbose_name='Project Phase Code')
    project_phase_title = models.CharField(max_length=55, blank=True, null=True, verbose_name='Project Phase Title')
    project_phase_venue = models.CharField(max_length=55, blank=True, null=True, verbose_name='Project Phase Venue')
    project_phase_start_dt = models.DateTimeField(blank=True, null=True, verbose_name='Project Phase Start Date')
    project_phase_finish_dt = models.DateTimeField(blank=True, null=True, verbose_name='Project Phase Finish Date')
    project_phase_comments = models.CharField(max_length=2000, blank=True, null=True,
                                              verbose_name='Project Phase Comments')
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='Project ID')

    class Meta:
        managed = True
        verbose_name_plural = 'Project Phases'
        db_table = 'project_phase'
        app_label = 'b_benchmarking'
        ordering = ['project_phase_code']

    def __str__(self):
        return str('%s' % self.project_phase_code)


class WBSLocationsForProjectPhases(models.Model):
    wbs_location_code_project_phase = models.CharField(unique=True, max_length=5,
                                                       verbose_name='WBS Location Code for Project Phase')
    wbs_location_title_project_phase = models.CharField(unique=True, blank=True, null=True, max_length=55,
                                                        verbose_name='WBS Location Title for Project Phase')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='WBS Location Comments')
    project_phase = models.ForeignKey(ProjectPhases, on_delete=models.CASCADE, verbose_name='Project Phase ID')

    class Meta:
        managed = True
        verbose_name_plural = "WBS Locations for Project Phases"
        db_table = 'wbs_location_project_phases'
        app_label = 'b_benchmarking'
        ordering = ['wbs_location_code_project_phase']

    def __str__(self):
        return f"{self.wbs_location_code_project_phase} - {self.wbs_location_title_project_phase}"


class CommodityWeightedUnitPriceAverages(models.Model):
    commodity_cameose = models.ForeignKey(CommodityCameose, on_delete=models.CASCADE,
                                          verbose_name='Commodity ID')
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='WUPA UOM ID', default=1)
    wupa_code = models.CharField(unique=True, max_length=5, verbose_name='WUPA Code')
    wupa_title = models.CharField(unique=True, max_length=55, verbose_name='WUPA Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Weighted Unit Price Averages"
        db_table = 'wupa_commodity'
        app_label = 'b_benchmarking'
        ordering = ['wupa_code']

    def __str__(self):
        return str('%s' % (self.wupa_code))


class CommodityWeightedUnitPriceAverageDetails(models.Model):
    wupa_commodity = models.ForeignKey(CommodityWeightedUnitPriceAverages,
                                       on_delete=models.CASCADE, verbose_name='WUPA Commodity ID')
    no_of_contracts = models.IntegerField(blank=True, null=True, default=0, verbose_name='Number of Contracts')
    qty = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True, verbose_name='Quantity')
    all_in_costs = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True,
                                       verbose_name='All-In Costs')
    avg_bid = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True,
                                  verbose_name='Avergare Bid Cost per UOM')
    geo_region = models.CharField(max_length=55, blank=True, null=True, verbose_name='Geographical Location')
    capture_dt = models.DateTimeField(blank=True, null=True, verbose_name='Capture Date')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Weighted Unit Price Average Commodity Details"
        db_table = 'wupa_commodity_details'
        app_label = 'b_benchmarking'

    def __str__(self):
        return str('%s' % self.comments)


class ProjectDataRepositoryCostItems(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE,
                                   verbose_name='Discipline ID', default=1)
    wbs_location_project_phases = models.ForeignKey(WBSLocationsForProjectPhases, on_delete=models.CASCADE,
                                                    verbose_name='WBS Location ID for Project Phases', default=1)
    commodity_cameose = models.ForeignKey(CommodityCameose, on_delete=models.CASCADE,
                                          verbose_name='Commodity Deliverable ID')
    supplier = models.ForeignKey(Company, on_delete=models.CASCADE,
                                 verbose_name='Supplier ID', default=1)
    pdr_cost_item_code = models.CharField(unique=False, max_length=5, verbose_name='PDR Cost Item Code')
    pdr_cost_item_title = models.CharField(unique=False, max_length=200, blank=True, null=True,
                                           verbose_name='PDR Cost Item Title')
    qty = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True, verbose_name='Quantity')
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE,
                            verbose_name='EBWP UOM ID', default=1)
    all_in_costs = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True,
                                       verbose_name='All-In Costs')
    unit_price = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True,
                                     verbose_name='Unit Price')
    geo_region = models.CharField(max_length=55, blank=True, null=True, verbose_name='Geographical Location')
    capture_dt = models.DateTimeField(blank=True, null=True, verbose_name='Capture Date')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "PDR Cost Items"
        db_table = 'pdr_cost_item'
        app_label = 'b_benchmarking'
        unique_together = [['commodity_cameose',
                            'supplier',
                            'pdr_cost_item_code',
                            'capture_dt',
                            ]]
        ordering = ['pdr_cost_item_code']

    def __str__(self):
        return str('%s' % self.pdr_cost_item_code)


class ProjectDataRepositoryCostItemDetails(models.Model):
    pdr_cost_item = models.ForeignKey(ProjectDataRepositoryCostItems, on_delete=models.CASCADE,
                                      verbose_name='PDR Cost Item ID', default=1)
    item_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
                                  blank=True, null=True, verbose_name='Item Item No')
    item_title = models.CharField(unique=False, max_length=200, blank=True, null=True,
                                  verbose_name='Item Item Title')
    qty = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True, verbose_name='Quantity')
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='EBWP UOM ID', default=1)
    labour_costs = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True,
                                       verbose_name='Labour Costs')
    material_costs = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True,
                                         verbose_name='Material Costs')
    equipment_costs = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True,
                                          verbose_name='Equipment Costs')
    cmr_costs = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True,
                                    verbose_name='Contingency and Management Reserve Costs')
    ohp_costs = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True,
                                    verbose_name='Overhead and Profit Costs')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "PDR Cost Item Labour Details"
        db_table = 'pdr_cost_item_details'
        app_label = 'b_benchmarking'
        unique_together = [['pdr_cost_item',
                            'item_no', ]]
        ordering = ['item_no']

    def __str__(self):
        return str(
            '%s %s' % (self.pdr_cost_item, self.item_no,))
