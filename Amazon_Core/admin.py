from django.contrib import admin
from .models import Question, Choice, demo, CustomerProfile, BillingAddress, ShippingAddress, CreditCard, school, teacher, Order, Timestamps,Shipment



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

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(demo)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(CreditCard)
admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
admin.site.register(school)
admin.site.register(teacher)
admin.site.register(Order)
admin.site.register(Shipment)
admin.site.register(Timestamps)

