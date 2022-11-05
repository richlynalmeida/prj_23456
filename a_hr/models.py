from django.db import models
from django.core.validators import RegexValidator


class StakeholderRoles(models.Model):
    stakeholder_role_code = models.CharField(unique=True, max_length=2, verbose_name='Stakeholder Role Code')
    stakeholder_role_title = models.CharField(unique=True, blank=True, null=True, max_length=20,
                                              verbose_name='Stakeholder Role Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Stakeholder Roles"
        db_table = 'stakeholder_role'
        app_label = 'a_hr'
        ordering = ['stakeholder_role_code']

    # def __str__(self):
    #     return str('%s' % self.stakeholder_role_code)
    def __str__(self):
        return f"{self.stakeholder_role_code} - {self.stakeholder_role_title}"


class Privilege(models.Model):
    privilege_code = models.CharField(unique=True, max_length=1, verbose_name='Privilege Code')
    privilege_title = models.CharField(unique=True, max_length=55, verbose_name='Privilege Title')

    class Meta:
        managed = True
        verbose_name_plural = "Privileges"
        db_table = 'privilege'
        app_label = 'a_hr'
        ordering = ['privilege_code']

    # def __str__(self):
    #     return str('%s' % self.privilege_code)
    def __str__(self):
        return f"{self.privilege_code} - {self.privilege_title}"


class CompanyCategory(models.Model):
    company_cat_code = models.CharField(unique=True, max_length=1, verbose_name='Company Category Code')
    company_cat_title = models.CharField(unique=True, max_length=55, verbose_name='Company Category Title')

    class Meta:
        managed = True
        verbose_name_plural = "Company Categories"
        db_table = 'company_category'
        app_label = 'a_hr'
        ordering = ['company_cat_code']

    # def __str__(self):
    #     return str('%s' % self.company_cat_code)
    def __str__(self):
        return f"{self.company_cat_code} - {self.company_cat_title}"


class Company(models.Model):
    company_category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE,
                                         verbose_name='Company Category ID')
    company_code = models.CharField(unique=True, max_length=3, verbose_name='Company Code')
    company_title = models.CharField(unique=True, max_length=55, verbose_name='Company Title')
    email = models.EmailField(max_length=254, verbose_name='Company E-mail', blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    business_phone = models.CharField(validators=[phoneNumberRegex], max_length=16, verbose_name='Business Phone')
    fax_number = models.CharField(validators=[phoneNumberRegex], max_length=16, verbose_name='Fax Number',
                                  blank=True, null=True)
    address1 = models.CharField(verbose_name='Address Line 1', blank=True, null=True, max_length=1024)
    address2 = models.CharField(verbose_name='Address Line 2', blank=True, null=True, max_length=1024)
    zip_postal_code = models.CharField(verbose_name='ZIP/Postal Code', max_length=15, blank=True, null=True)
    city = models.CharField(verbose_name='City', max_length=50, blank=True, null=True)
    state_province = models.CharField(verbose_name='State/Province', max_length=50, blank=True, null=True)
    country = models.CharField(verbose_name='Country', max_length=50, blank=True, null=True)
    web_page = models.URLField(blank=True, null=True, max_length=250,
                               verbose_name='Wep Page')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Companies"
        db_table = 'company'
        app_label = 'a_hr'
        ordering = ['company_code']

    # def __str__(self):
    #     return str('%s' % self.company_code)
    def __str__(self):
        return f"{self.company_code} - {self.company_title}"


class PersonnelCategory(models.Model):
    personnel_cat_code = models.CharField(unique=True, max_length=1, verbose_name='Personnel Category Code')
    personnel_cat_title = models.CharField(unique=True, max_length=55, verbose_name='Personnel Category Title')

    class Meta:
        managed = True
        verbose_name_plural = "Personnel Categories"
        db_table = 'personnel_category'
        app_label = 'a_hr'
        ordering = ['personnel_cat_code']

    # def __str__(self):
    #     return str('%s' % self.personnel_cat_code)
    def __str__(self):
        return f"{self.personnel_cat_code} - {self.personnel_cat_title}"


class Personnel(models.Model):
    personnel_category = models.ForeignKey(PersonnelCategory, on_delete=models.CASCADE,
                                           verbose_name='Personnel Category ID')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Company ID')
    personnel_code = models.CharField(unique=True, max_length=3, verbose_name='Personnel Code')
    personnel_title = models.CharField(unique=False, max_length=55, verbose_name='Personnel Title')
    first_name = models.CharField(verbose_name='First Name', max_length=50, blank=True, null=True)
    middle_name = models.CharField(verbose_name='Middle Name', max_length=50, blank=True, null=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, verbose_name='E-mail', blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    business_phone = models.CharField(validators=[phoneNumberRegex], max_length=16, blank=True, null=True,
                                      verbose_name='Business Phone')
    home_phone = models.CharField(validators=[phoneNumberRegex], max_length=16, blank=True, null=True,
                                  verbose_name='Home Phone')
    mobile_phone = models.CharField(validators=[phoneNumberRegex], max_length=16, blank=True, null=True,
                                    verbose_name='Mobile Phone')
    address1 = models.CharField(verbose_name='Address Line 1', blank=True, null=True, max_length=1024)
    address2 = models.CharField(verbose_name='Address Line 2', blank=True, null=True, max_length=1024)
    zip_postal_code = models.CharField(verbose_name='ZIP/Postal Code', max_length=15, blank=True, null=True)
    city = models.CharField(verbose_name='City', max_length=50, blank=True, null=True)
    state_province = models.CharField(verbose_name='State/Province', max_length=50, blank=True, null=True)
    country = models.CharField(verbose_name='Country', max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Personnel"
        db_table = 'personnel'
        app_label = 'a_hr'
        ordering = ['personnel_code']

    # def __str__(self):
    #     return str('%s' % self.personnel_code)
    def __str__(self):
        return f"{self.personnel_code} - {self.personnel_title}"


class RaciMatrixDefinition(models.Model):
    raci_code = models.CharField(unique=True, max_length=1, verbose_name='RACI Code')
    raci_title = models.CharField(unique=True, max_length=15, verbose_name='RACI Title')

    class Meta:
        managed = True
        verbose_name_plural = "RACI Matrix Definition"
        db_table = 'raci_matrix_definition'
        app_label = 'a_hr'
        ordering = ['raci_code']

    # def __str__(self):
    #     return str('%s' % self.raci_code)
    def __str__(self):
        return f"{self.raci_code} - {self.raci_title}"
