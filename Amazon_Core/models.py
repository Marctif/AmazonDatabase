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
    Street = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zipcode = models.IntegerField()

class BillingAddress(models.Model):
    custProfile = models.ForeignKey(CustomerProfile)
    Street = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zipcode = models.IntegerField()

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
    ("JAN", "1"),
    ("FEB", "2"),
    ("APR", "3"),
    ("MAY", "4"),
    ("JUNE", "5"),

)

class CreditCard(models.Model):
    custProfile = models.ForeignKey(CustomerProfile)
    CreditCardNumber = models.IntegerField()
    SecurityCode = models.IntegerField()
    ExpMonth = models.IntegerField(choices=MONTHS, default=1)
    ExpYear = models.IntegerField(choices=YEARS, default=2017)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class demo(models.Model):
    idTest = models.IntegerField(default=0)
    text = models.CharField(max_length=200)