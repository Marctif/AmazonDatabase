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
    lineitem = models.CharField(max_length=50,default = None)
    custProfile = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    payMethod = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.lineitem

class Shipment(models.Model):
    STATUS = (
        ('OR', 'Ordered'),
        ('SP', 'Shipped'),
        ('DE', 'Delivered'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=5, choices=STATUS, default='OR',)
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

