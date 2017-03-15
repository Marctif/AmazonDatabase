from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .choices import *
# Create your models here.

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class ShippingAddress(models.Model):
    custProfile = models.ForeignKey(CustomerProfile)
    Street = models.CharField(max_length=50, null=True)
    City = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=50, null=True)
    Zipcode = models.IntegerField(null=True)
    count = models.IntegerField(null=True)

    def __str__(self):
        return self.Street + " " + self.City + " " + self.State + " " + str(self.Zipcode)

class BillingAddress(models.Model):
    custProfile = models.ForeignKey(CustomerProfile)
    Street = models.CharField(max_length=50, null=True)
    City = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=50, null=True)
    Zipcode = models.IntegerField( null=True)
    count = models.IntegerField(null=True)

    def __str__(self):
        return self.Street + " " + self.City + " " + self.State + " " + str(self.Zipcode)



class CreditCard(models.Model):
    custProfile = models.ForeignKey(CustomerProfile)
    CreditCardNumber = models.IntegerField(null=True)
    SecurityCode = models.IntegerField(null=True)
    ExpMonth = models.IntegerField(choices=MONTHS, default=1,null=True)
    ExpYear = models.IntegerField(choices=YEARS, default=2017,null=True)

    def __str__(self):
        return str(self.CreditCardNumber)

class Order(models.Model):
    STATUS = (
                ('PE', 'PENDING'),
                ('SH', 'SHIPPED'),
                ('IN', 'INVOICED'),
                ('RE', 'RETURNED'),
        )

    custProfile = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    billAddress = models.ForeignKey(BillingAddress,on_delete=models.CASCADE, null=True)
    shipAddress = models.ForeignKey(ShippingAddress,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='PE', )
    payMethod = models.ForeignKey(CreditCard, on_delete=models.CASCADE, null=True)
    total_cost = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.custProfile.first_name + " " + self.custProfile.last_name + " - $" + str(self.total_cost) + " ("+ self.get_status_display() + ") "

class Item(models.Model):
    SKU = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    numAvailable = models.IntegerField()
    picture = models.ImageField(upload_to='items', null=True, )

    def __str__(self):
        return self.name

class LineItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    cost = models.IntegerField(null=True)
    subTotal = models.IntegerField(null=True)

    def __str__(self):
        return self.item.name + " - " + str(self.quantity) + " @ $" + str(self.cost) + " per"

class LineItemTable(models.Model):
    item = models.ForeignKey(Item)
    lineItem = models.ForeignKey(LineItem)

class Shipment(models.Model):
    STATUS = (
        ('PI', 'Pick'),
        ('PA', 'Pack'),
        ('SH', 'Ship'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    litem = models.ForeignKey(LineItem, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=5, choices=STATUS, default='PI',)
    estimated_date = models.DateField(default=datetime.now, blank=True)
    shipped_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.order.id) + " - " + str(self.litem) + " - " + self.get_status_display()


# TEST FOR DYNAMOC ADDING TO FORMSET
class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class TodoItem(models.Model):
    name = models.CharField(max_length=150,
               help_text="e.g. Buy milk, wash dog etc")
    list = models.ForeignKey(TodoList)

    def __unicode__(self):
        return self.name + " (" + str(self.list) + ")"