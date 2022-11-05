from django.contrib import admin
from . import models
from django import forms

from .models import PurchaseOrder

admin.site.register(models.PurchaseOrderStatus)
admin.site.register(models.PayMethod)
admin.site.register(models.InventoryTransactionType)
admin.site.register(models.OrderTaxStatus)
admin.site.register(models.OrderStatus)
admin.site.register(models.OrderDetailStatus)
admin.site.register(models.MaterialStatus)


def PaymentAmountWithDollarSign(obj): # Here
    return "$" + str(obj.payment_amount)


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = [
        'po_commit_code',
        'po_commit_title',
        'supplier',
        'create_by_personnel',
        'create_date',
        'submit_date',
        'purchase_order_status',
        'expect_date',
        'shipping_fee',
        'taxes',
        'payment_date',
        'payment_amount',
        'pay_method',
        'comments',
        'approve_by_personnel',
        'approve_date',
        'submit_by_personnel',
        'PaymentAmountWithDollarSign' # Don't forget to put
    ]
# admin.site.register(models.PurchaseOrder)


