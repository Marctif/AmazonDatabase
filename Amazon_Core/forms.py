from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="first_name", required=True)
    last_name = forms.CharField(label="last_name", required=True)
    email = forms.CharField(label="email", required=True)
    password = forms.CharField(label="password",widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        # get form values
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError("This user does not exist")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect Password")
        if not user.is_active:
            raise forms.ValidationError("This user no longer exists")
        return super(UserLoginForm, self).clean(*args, **kwargs)

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

YEARS = (
    (2017, "2017"),
    (2018, "2018"),
    (2019, "2019"),
    (2020, "2020"),
    (2021, "2021"),
    (2022, "2022"),
    (2023, "2023"),
)
MONTHS = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),

)

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

