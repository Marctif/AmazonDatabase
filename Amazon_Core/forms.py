from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.forms import ModelForm
from .models import *
from .choices import *


class CustomerProfileForm(forms.Form):
    first_name = forms.CharField(label="First name", required=True)
    last_name = forms.CharField(label="Last name", required=True)
    birthday = forms.DateField(label="Birthday", required=True)


    def clean(self):
        cleaned_data = super(CustomerProfileForm, self).clean()

        # get form values
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        birthday = cleaned_data.get('date')


class ShippingAddressForm(forms.Form):
    street = forms.CharField(label="street", required=True)
    city = forms.CharField(label="city", required=True)
    state = forms.CharField(label="state", required=True)
    zipcode = forms.IntegerField(label="zipcode", required=True)

    def clean(self):
        cleaned_data = super(ShippingAddressForm, self).clean()

        # get form values
        street = cleaned_data.get('street')
        city = cleaned_data.get('city')
        state = cleaned_data.get('state')
        zipcode = cleaned_data.get('zipcode')

class BillingAddressForm(forms.Form):
    streetB = forms.CharField(label="street", required=True)
    cityB = forms.CharField(label="city", required=True)
    stateB = forms.CharField(label="state", required=True)
    zipcodeB = forms.IntegerField(label="zipcode", required=True)

    def clean(self):
        cleaned_data = super(BillingAddressForm, self).clean()

        # get form values
        streetB = cleaned_data.get('streetB')
        cityB = cleaned_data.get('cityB')
        stateB = cleaned_data.get('stateB')
        zipcodeB = cleaned_data.get('zipcodeB')


class CreditCardForm(forms.Form):
    number = forms.IntegerField(label="Credit card Number")
    securityCode = forms.IntegerField(label="Security Code")
    month = forms.ChoiceField(choices=MONTHS, label="Month", initial='', widget=forms.Select(), required=True)
    year = forms.ChoiceField(choices=YEARS, label="Years", initial='', widget=forms.Select(), required=True)

    def clean(self):
        cleaned_data = super(CreditCardForm, self).clean()

        # get form values
        number = cleaned_data.get('number')
        securityCode = cleaned_data.get('securityCode')
        month = cleaned_data.get('month')
        year = cleaned_data.get('year')

class ItemForm(forms.Form):
    price = forms.IntegerField(label="Price")
    numAvailable = forms.IntegerField(label="Total number available")

    def clean(self):
        cleaned_data = super(ItemForm, self).clean()

        # get form values
        price = cleaned_data.get('price')
        numAvailable = cleaned_data.get('numAvailable')

class TodoListForm(ModelForm):
  class Meta:
    model = TodoList
    fields = '__all__'


class TodoItemForm(ModelForm):
  class Meta:
    model = TodoItem
    exclude = ('list',)
    fields = '__all__'

class ShippingForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        exclude = ('custProfile', 'count',)

class BillingForm(ModelForm):
    class Meta:
        model = BillingAddress
        fields = '__all__'
        exclude = ('custProfile', 'count',)

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('custProfile','status','total_cost')

    def __init__(self, custProfile, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['billAddress'].queryset = BillingAddress.objects.filter(custProfile=custProfile)
        self.fields['shipAddress'].queryset = ShippingAddress.objects.filter(custProfile=custProfile)
        self.fields['payMethod'].queryset = CreditCard.objects.filter(custProfile=custProfile)

