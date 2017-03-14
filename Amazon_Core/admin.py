from django.contrib import admin
from .models import CustomerProfile, BillingAddress, ShippingAddress, CreditCard, Order,Shipment, Item,LineItem



class ShippingAddressInline(admin.TabularInline):
    model = ShippingAddress
    extra = 1

class BillingAddressInline(admin.TabularInline):
    model = BillingAddress
    extra = 1

class CreditCardInline(admin.TabularInline):
    model = CreditCard
    extra = 1

class CustomerProfileAdmin(admin.ModelAdmin):
    inlines = [ShippingAddressInline, BillingAddressInline, CreditCardInline]

admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(CreditCard)
admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(Shipment)
admin.site.register(Item)
admin.site.register(LineItem)


