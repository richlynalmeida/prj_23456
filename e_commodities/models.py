from django.db import models


class CommodityTypeCameose(models.Model):
    commodity_type_code_cameose = models.CharField(unique=True, max_length=5,
                                                   verbose_name='Cameose Commodity Type Code')
    commodity_type_title_cameose = models.CharField(unique=True, max_length=155, blank=True, null=True,
                                                    verbose_name='Cameose Commodity Type Title')

    class Meta:
        managed = True
        verbose_name_plural = "Commodity Types - Cameose"
        db_table = 'commodity_type_cameose'
        app_label = 'e_commodities'
        ordering = ['commodity_type_code_cameose']

    # def __str__(self):
    #     return str('%s' % self.commodity_type_code_cameose)
    def __str__(self):
        return f"{self.commodity_type_code_cameose} - {self.commodity_type_title_cameose}"


class CommodityCameose(models.Model):
    commodity_type_cameose = models.ForeignKey(CommodityTypeCameose, on_delete=models.CASCADE,
                                               verbose_name='Cameose Commodity Type ID')
    commodity_code_cameose = models.CharField(unique=True, max_length=15, verbose_name='Cameose Commodity Code')
    commodity_title_cameose = models.CharField(unique=True, max_length=155, blank=True, null=True,
                                               verbose_name='Cameose Commodity Title')

    class Meta:
        managed = True
        verbose_name_plural = "Commodities - Cameose"
        db_table = 'commodity_cameose'
        app_label = 'e_commodities'
        ordering = ['commodity_code_cameose']

    # def __str__(self):
    #     return str('%s' % self.commodity_code_cameose)
    def __str__(self):
        return f"{self.commodity_code_cameose} - {self.commodity_title_cameose}"


class CommodityDetailCameose(models.Model):
    commodity_cameose = models.ForeignKey(CommodityCameose, on_delete=models.CASCADE,
                                          verbose_name='Cameose Commodity ID')
    commodity_detail_code_cameose = models.CharField(unique=True, max_length=15,
                                                     verbose_name='Cameose Commodity Detail Code')
    commodity_detail_title_cameose = models.CharField(unique=True, max_length=155, blank=True, null=True,
                                                      verbose_name='Cameose Commodity Detail Title')

    class Meta:
        managed = True
        verbose_name_plural = "Commodity Details - Cameose"
        db_table = 'commodity_detail_cameose'
        app_label = 'e_commodities'
        ordering = ['commodity_detail_code_cameose']

    # def __str__(self):
    #     return str('%s' % self.commodity_detail_code_cameose)
    def __str__(self):
        return f"{self.commodity_detail_code_cameose} - {self.commodity_detail_title_cameose}"


class CommodityType(models.Model):
    commodity_type_code = models.CharField(unique=True, max_length=5, verbose_name='Commodity Type Code')
    commodity_type_title = models.CharField(unique=True, max_length=155, blank=True, null=True,
                                            verbose_name='Commodity Type Title')

    class Meta:
        managed = True
        verbose_name_plural = "Commodity Types"
        db_table = 'commodity_type'
        app_label = 'e_commodities'
        ordering = ['commodity_type_code']

    # def __str__(self):
    #     return str('%s' % self.commodity_type_code)
    def __str__(self):
        return f"{self.commodity_type_code} - {self.commodity_type_title}"


class Commodity(models.Model):
    commodity_type = models.ForeignKey(CommodityType, on_delete=models.CASCADE,
                                       verbose_name='Commodity Type ID')
    commodity_code = models.CharField(unique=True, max_length=15, verbose_name='Commodity Code')
    commodity_title = models.CharField(unique=True, max_length=155, blank=True, null=True,
                                       verbose_name='Commodity Title')

    class Meta:
        managed = True
        verbose_name_plural = "Commodities"
        db_table = 'commodity'
        app_label = 'e_commodities'
        ordering = ['commodity_code']

    # def __str__(self):
    #     return str('%s' % self.commodity_code)
    def __str__(self):
        return f"{self.commodity_code} - {self.commodity_title}"


class CommodityDetail(models.Model):
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE,
                                  verbose_name='Commodity ID')
    commodity_detail_code = models.CharField(unique=True, max_length=15,
                                             verbose_name='Commodity Detail Code')
    commodity_detail_title = models.CharField(unique=True, max_length=155, blank=True, null=True,
                                              verbose_name='Commodity Detail Title')

    class Meta:
        managed = True
        verbose_name_plural = "Commodity Details"
        db_table = 'commodity_detail'
        app_label = 'e_commodities'
        ordering = ['commodity_detail_code']

    # def __str__(self):
    #     return str('%s' % self.commodity_detail_code)
    def __str__(self):
        return f"{self.commodity_detail_code} - {self.commodity_detail_title}"