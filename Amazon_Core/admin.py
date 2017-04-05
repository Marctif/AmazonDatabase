from django.contrib import admin
from .models import *


class ShippingAddressInline(admin.TabularInline):
    model = ShippingAddress
    extra = 1

class BillingAddressInline(admin.TabularInline):
    model = BillingAddress
    extra = 1

class CreditCardInline(admin.TabularInline):
    model = CreditCard
    extra = 1

class ShipmentInline(admin.TabularInline):
    model = Shipment
    extra = 0

class SubItemInline(admin.TabularInline):
    model = SubscriptionItem
    extra = 0

class SubsciptionAdmin(admin.ModelAdmin):
    inlines = [SubItemInline]

class CustomerProfileAdmin(admin.ModelAdmin):
    inlines = [ShippingAddressInline, BillingAddressInline, CreditCardInline]

class OrderAdmin(admin.ModelAdmin):
    inlines = [ShipmentInline]

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['__str__','status']


admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(CreditCard)
admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
admin.site.register(Order, OrderAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Item)
admin.site.register(LineItem)
admin.site.register(Subscription, SubsciptionAdmin)
admin.site.register(SubscriptionItem)


