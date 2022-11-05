from django.db import models


class Department(models.Model):
    department_code = models.CharField(unique=True, max_length=5, verbose_name='Department Code', )
    department_title = models.CharField(unique=True, max_length=55, verbose_name='Department Title', )

    class Meta:
        managed = True
        verbose_name_plural = "Departments"
        db_table = 'department'
        app_label = 'b_wbs'
        ordering = ['department_code']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.department_code} - {self.department_title}"


class Discipline(models.Model):
    discipline_code = models.CharField(unique=True, max_length=5, verbose_name='Discipline Code')
    discipline_title = models.CharField(unique=True, max_length=55, verbose_name='Discipline Title')

    class Meta:
        managed = True
        verbose_name_plural = "Disciplines"
        db_table = 'discipline'
        app_label = 'b_wbs'
        ordering = ['discipline_code']

    # def __str__(self):
    #     return str('%s' % self.discipline_code)
    def __str__(self):
        return f"{self.discipline_code} - {self.discipline_title}"


class WBSLocation(models.Model):
    wbs_location_code = models.CharField(unique=True, max_length=5, verbose_name='WBS Location Code')
    wbs_location_title = models.CharField(unique=True, blank=True, null=True, max_length=55,
                                          verbose_name='WBS Location Title')

    class Meta:
        managed = True
        verbose_name_plural = "WBS Locations"
        db_table = 'wbs_location'
        app_label = 'b_wbs'
        ordering = ['wbs_location_code']

    # def __str__(self):
    #     return str('%s' % self.wbs_location_code)
    def __str__(self):
        return f"{self.wbs_location_code} - {self.wbs_location_title}"


class CostTypeClass(models.Model):
    cost_type_class_code = models.CharField(unique=True, max_length=2, verbose_name='Cost Type Class Code')
    cost_type_class_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                             verbose_name='Cost Type Class Title')

    class Meta:
        managed = True
        verbose_name_plural = "Cost Type Classes"
        db_table = 'cost_type_class'
        app_label = 'b_wbs'
        ordering = ['cost_type_class_code']

    # def __str__(self):
    #     return str('%s' % self.cost_type_class_code)
    def __str__(self):
        return f"{self.cost_type_class_code} - {self.cost_type_class_title}"


class CostType(models.Model):
    cost_type_class = models.ForeignKey(CostTypeClass, on_delete=models.CASCADE,
                                          verbose_name='Cost Type Class ID')
    cost_type_code = models.CharField(unique=True, max_length=5, verbose_name='Cost Type Code')
    cost_type_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                             verbose_name='Cost Type Title')

    class Meta:
        managed = True
        verbose_name_plural = "Cost Types"
        db_table = 'cost_type'
        app_label = 'b_wbs'
        ordering = ['cost_type_code']

    # def __str__(self):
    #     return str('%s' % self.cost_type_code)
    def __str__(self):
        return f"{self.cost_type_code} - {self.cost_type_title}"


class FacilitySystem(models.Model):
    facility_system_code = models.CharField(unique=True, max_length=5, verbose_name='Facility System Code')
    facility_system_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                             verbose_name='Facility System Title')

    class Meta:
        managed = True
        verbose_name_plural = "Facility Systems"
        db_table = 'facility_system'
        app_label = 'b_wbs'
        ordering = ['facility_system_code']

    # def __str__(self):
    #     return str('%s' % self.facility_system_code)
    def __str__(self):
        return f"{self.facility_system_code} - {self.facility_system_title}"


class FacilitySystemDetail(models.Model):
    facility_system = models.ForeignKey(FacilitySystem, on_delete=models.CASCADE, verbose_name='Facility System ID')
    facility_system_detail_code = models.CharField(unique=True, max_length=15,
                                                   verbose_name='Facility System Detail Code')
    facility_system_detail_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                                    verbose_name='Facility System Detail Title')

    class Meta:
        managed = True
        verbose_name_plural = "Facility System Details"
        db_table = 'facility_system_detail'
        app_label = 'b_wbs'
        ordering = ['facility_system_detail_code']
        unique_together = [['facility_system', 'facility_system_detail_code']]

    # def __str__(self):
    #     return str('%s' % self.facility_system_detail_code)
    def __str__(self):
        return f"{self.facility_system_detail_code} - {self.facility_system_detail_title}"


class EBWPType(models.Model):
    ebwp_type_code = models.CharField(unique=True, max_length=5, verbose_name='EBWP Type Code')
    ebwp_type_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                       verbose_name='EBWP Type Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='EBWP Type Comments')

    class Meta:
        managed = True
        verbose_name_plural = "EBWP Types"
        db_table = 'ebwp_type'
        app_label = 'b_wbs'
        ordering = ['ebwp_type_code']

    # def __str__(self):
    #     return str('%s' % self.ebwp_type_code)
    def __str__(self):
        return f"{self.ebwp_type_code} - {self.ebwp_type_title}"


class EBWPStatus(models.Model):
    ebwp_status_code = models.CharField(unique=True, max_length=5, verbose_name='EBWP Status Code')
    ebwp_status_title = models.CharField(unique=True, max_length=55, verbose_name='EBWP Status Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='EBWP Status Comments')

    class Meta:
        managed = True
        verbose_name_plural = "EB Work Package Statuses"
        db_table = 'ebwp_status'
        app_label = 'b_wbs'
        ordering = ['ebwp_status_code']

    # def __str__(self):
    #     return str('%s' % self.ebwp_status_code)
    def __str__(self):
        return f"{self.ebwp_status_code} - {self.ebwp_status_title}"


class CBWPType(models.Model):
    ebwp_type = models.ForeignKey(EBWPType, on_delete=models.CASCADE, verbose_name='EBWP Type ID')
    cbwp_type_code = models.CharField(unique=True, max_length=5, verbose_name='CBWP Type Code')
    cbwp_type_title = models.CharField(unique=True, max_length=55, verbose_name='CBWP Type Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='CBWP Type Comments')

    class Meta:
        managed = True
        verbose_name_plural = "CBWP Types"
        db_table = 'cbwp_type'
        app_label = 'b_wbs'
        ordering = ['cbwp_type_code']

    # def __str__(self):
    #     return str('%s' % self.cbwp_type_code)
    def __str__(self):
        return f"{self.cbwp_type_code} - {self.cbwp_type_title}"


class CBWPStatus(models.Model):
    cbwp_status_code = models.CharField(unique=True, max_length=5, verbose_name='CBWP Status Code')
    cbwp_status_title = models.CharField(unique=True, max_length=55, verbose_name='CBWP Status Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='CBWP Status Comments')

    class Meta:
        managed = True
        verbose_name_plural = "CB Work Package Statuses"
        db_table = 'cbwp_status'
        app_label = 'b_wbs'
        ordering = ['cbwp_status_code']

    # def __str__(self):
    #     return str('%s' % self.cbwp_status_code)
    def __str__(self):
        return f"{self.cbwp_status_code} - {self.cbwp_status_title}"