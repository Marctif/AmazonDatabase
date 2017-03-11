from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
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

    def __str__(self):
        return self.Street + " " + self.City + " " + self.State + " " + str(self.Zipcode)

class BillingAddress(models.Model):
    custProfile = models.ForeignKey(CustomerProfile)
    Street = models.CharField(max_length=50, null=True)
    City = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=50, null=True)
    Zipcode = models.IntegerField( null=True)

    def __str__(self):
        return self.Street + " " + self.City + " " + self.State + " " + str(self.Zipcode)

YEARS = (
    ("2017", "2017"),
    ("2018", "2018"),
    ("2019", "2019"),
    ("2020", "2020"),
    ("2021", "2021"),
    ("2022", "2022"),
    ("2023", "2023"),
)
MONTHS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),

)

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
    status = models.CharField(max_length=10, choices=STATUS, default='PE',)
    payMethod = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    total_cost = models.PositiveIntegerField(default=0)
    tax = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.get_status_display() + " "

class Cart(models.Model):
    custProfile = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(default=0)

class Item(models.Model):
    SKU = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    numAvailable = models.IntegerField()

    def __str__(self):
        return self.name

class LineItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cost = models.IntegerField()

    def __str__(self):
        return self.item.name


class Shipment(models.Model):
    STATUS = (
        ('PI', 'Pick'),
        ('PA', 'Pack'),
        ('SH', 'Ship'),
    )
    litem = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    status = models.CharField(max_length=5, choices=STATUS, default='PI',)
    estimated_date = models.DateField(default=datetime.now, blank=True)
    shipped_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.get_status_display() + " " + self.order.lineitem

class Timestamps(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=True, default=datetime.now )
    description = models.CharField(max_length=50)
    City = models.CharField(max_length=10)
    State = models.CharField(max_length=10)

    def __str__(self):
        return self.shipment.order.lineitem + " " + self.description