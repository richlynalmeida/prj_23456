from django.db import models
from a_hr.models import Personnel, Company
from i_eb.models import EBWP
from django.core.validators import MinValueValidator, MaxValueValidator


class PurchaseOrderStatus(models.Model):
    purchase_order_status_code = models.CharField(unique=True, max_length=1, verbose_name='PO Status Code')
    purchase_order_status_title = models.CharField(unique=True, max_length=55, verbose_name='PO Status Title')

    class Meta:
        managed = True
        verbose_name_plural = "Purchase Order Statuses"
        db_table = 'purchase_order_status'
        app_label = 'd_mm'
        ordering = ['purchase_order_status_code']

    # def __str__(self):
    #     return str('%s' % self.purchase_order_status_code)
    def __str__(self):
        return f"{self.purchase_order_status_code} - {self.purchase_order_status_title}"


class InventoryTransactionType(models.Model):
    inventory_transaction_type_code = models.CharField(unique=True, max_length=1,
                                                       verbose_name='Inventory Transaction Type Code')
    inventory_transaction_type_title = models.CharField(unique=True, max_length=55,
                                                        verbose_name='Inventory Transaction Type Title')

    class Meta:
        managed = True
        verbose_name_plural = "Inventory Transaction Types"
        db_table = 'inventory_transaction_type'
        app_label = 'd_mm'
        ordering = ['inventory_transaction_type_code']

    #
    # def __str__(self):
    #     return str('%s' % self.inventory_transaction_type_code)
    def __str__(self):
        return f"{self.inventory_transaction_type_code} - {self.inventory_transaction_type_title}"


class OrderStatus(models.Model):
    order_status_code = models.CharField(unique=True, max_length=1, verbose_name='Orders Status Code')
    order_status_title = models.CharField(unique=True, max_length=55, verbose_name='Orders Status Title')

    class Meta:
        managed = True
        verbose_name_plural = "Orders Status"
        db_table = 'order_status'
        app_label = 'd_mm'
        ordering = ['order_status_code']

    # def __str__(self):
    #     return str('%s' % self.order_status_code)
    def __str__(self):
        return f"{self.order_status_code} - {self.order_status_title}"


class OrderDetailStatus(models.Model):
    order_detail_status_code = models.CharField(unique=True, max_length=1, verbose_name='Order Detail Status Code')
    order_detail_status_title = models.CharField(unique=True, max_length=55, verbose_name='Order Detail Status Title')

    class Meta:
        managed = True
        verbose_name_plural = "Order Details Status"
        db_table = 'order_detail_status'
        app_label = 'd_mm'
        ordering = ['order_detail_status_code']

    # def __str__(self):
    #     return str('%s' % self.order_detail_status_code)
    def __str__(self):
        return f"{self.order_detail_status_code} - {self.order_detail_status_title}"


class OrderTaxStatus(models.Model):
    order_tax_status_code = models.CharField(unique=True, max_length=1, verbose_name='Order Tax Status Code')
    order_tax_status_title = models.CharField(unique=True, max_length=55, verbose_name='Order Tax Status Title')

    class Meta:
        managed = True
        verbose_name_plural = "Orders Tax Status"
        db_table = 'order_tax_status'
        app_label = 'd_mm'
        ordering = ['order_tax_status_code']

    # def __str__(self):
    #     return str('%s' % self.order_tax_status_code)
    def __str__(self):
        return f"{self.order_tax_status_code} - {self.order_tax_status_title}"


class PayMethod(models.Model):
    pay_method_code = models.CharField(unique=True, max_length=1, verbose_name='Pay Method Code')
    pay_method_title = models.CharField(unique=True, max_length=55, verbose_name='Pay Method Title')

    class Meta:
        managed = True
        verbose_name_plural = "Payment Methods"
        db_table = 'pay_method'
        app_label = 'd_mm'
        ordering = ['pay_method_code']

    # def __str__(self):
    #     return str('%s' % self.pay_method_code)
    def __str__(self):
        return f"{self.pay_method_code} - {self.pay_method_title}"


class MaterialStatus(models.Model):
    material_status_code = models.CharField(unique=True, max_length=2, verbose_name='Material Status Code')
    material_status_title = models.CharField(unique=True, max_length=55, verbose_name='Material Status Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Material Statuses"
        db_table = 'material_status'
        app_label = 'd_mm'
        ordering = ['material_status_code']

    # def __str__(self):
    #     return str('%s' % self.material_status_code)
    def __str__(self):
        return f"{self.material_status_code} - {self.material_status_title}"


class PurchaseOrder(models.Model):
    po_commit_code = models.CharField(unique=True, max_length=55, verbose_name='PO/Commit Package Code')
    po_commit_title = models.CharField(unique=True, max_length=200, verbose_name='PO/Commit Package Title')
    supplier = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Supplier ID')
    create_by_personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE,
                                            verbose_name='Created By', related_name='create_by_personnel')
    create_date = models.DateTimeField(blank=True, null=True, verbose_name='PO Creation Date')
    submit_date = models.DateTimeField(blank=True, null=True, verbose_name='PO Submission Date')
    purchase_order_status = models.ForeignKey(PurchaseOrderStatus, on_delete=models.CASCADE,
                                              verbose_name='Purchase Order Status ID')
    expect_date = models.DateTimeField(blank=True, null=True, verbose_name='Order Expected Date')
    shipping_fee = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                       verbose_name='Shipping Fee',
                                       default=0)
    taxes = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                verbose_name='Taxes',
                                default=0)
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='Payment Date')
    payment_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                         validators=[MinValueValidator(1), MaxValueValidator(999999999)],
                                         verbose_name='Payment Amount',
                                         default=0)
    pay_method = models.ForeignKey(PayMethod, on_delete=models.CASCADE, verbose_name='Pay Method ID')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')
    approve_by_personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE,
                                             verbose_name='Approved By', related_name='approve_by_personnel')
    approve_date = models.DateTimeField(blank=True, null=True, verbose_name='Approval Date')
    submit_by_personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE,
                                            verbose_name='Submitted By', related_name='submit_by_personnel')

    class Meta:
        managed = True
        verbose_name_plural = "Purchase Orders - Commit Packages"
        db_table = 'purchase_order'
        app_label = 'd_mm'
        ordering = ['po_commit_code']

    def __str__(self):
        return str('%s' % self.po_commit_code)

    @property # Here
    def PaymentAmountWithDollarSign(self):
        return "$" + str(self.payment_amount)
