from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, UserLoginForm, CustomerProfileForm, ShippingAddressForm, CreditCardForm, BillingAddressForm, ItemForm
from .models import CustomerProfile, ShippingAddress, CreditCard, BillingAddress, MONTHS, YEARS, Item
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404
import datetime

# Create your views here.

def home(request):
    return render(request, 'Amazon_Core/home.html')

def demo(request):
    return render(request, 'Amazon_Core/demo.html')

def update_profile(request):
    return render(request, 'Amazon_Core/update_profile.html')

def login_view(request):
    form = UserLoginForm(request.POST or None)
    print(request.user)
    print(request.user.is_authenticated)

    if form.is_valid():
        #print("Form is valid")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect ('home')

    return render(request, 'Amazon_Core/login.html', {"form": form})


def signup(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            first_name_Val= form.cleaned_data.get('first_name')
            last_name_Val = form.cleaned_data.get('last_name')
            email_Val = form.cleaned_data.get('email')
            password_Val = form.cleaned_data.get('password')

            try:
                user = User.objects.create_user(
                    first_name = first_name_Val,
                    last_name = last_name_Val,
                    email = email_Val,
                    password = password_Val,
                    username = email_Val
                )
                profile = CustomerProfile.objects.create(user=user)


            except ValueError:
                print(ValueError)
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
    return render(request, 'Amazon_Core/signup.html',  {'form': form })

def update_profile_temp(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        #custProfile = CustomerProfile.objects.filter(user=request.user)

        form1 = CustomerProfileForm(request.POST)
        form2 = ShippingAddressForm(request.POST)
        form3 = CreditCardForm(request.POST)
        form4 = BillingAddressForm(request.POST)
        # check whether it's valid:
        if form1.is_valid() & form2.is_valid() & form4.is_valid() & form3.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            first_name_Val= form1.cleaned_data.get('first_name')
            last_name_Val = form1.cleaned_data.get('last_name')
            birthday_Val = form1.cleaned_data.get('birthday')


            StreetS = form2.cleaned_data.get('street')
            StateS = form2.cleaned_data.get('state')
            CityS = form2.cleaned_data.get('city')
            ZipcodeS = form2.cleaned_data.get('zipcode')

            StreetB = form4.cleaned_data.get('streetB')
            StateB = form4.cleaned_data.get('stateB')
            CityB = form4.cleaned_data.get('cityB')
            ZipcodeB = form4.cleaned_data.get('zipcodeB')

            number_Val = form3.cleaned_data.get("number")
            securityCode_Val = form3.cleaned_data.get("securityCode")
            month_Val = form3.cleaned_data.get("month")
            year_Val = form3.cleaned_data.get("year")

            #street_Val = form2.cleaned_data.get('street')
            #print(first_name_Val)
           # print (street_Val)
            #last_name_Val = form.cleaned_data.get('last_name')
            #email_Val = form.cleaned_data.get('email')
            #password_Val = form.cleaned_data.get('password')

            if(CustomerProfile.objects.filter(user=request.user).first() == None):
                CustomerProfile.objects.create(
                    user=request.user,
                    first_name=""
                )
            custProfile = get_object_or_404(CustomerProfile, user=request.user)

            custProfile.first_name = first_name_Val
            custProfile.save(update_fields=["first_name"])
            custProfile.last_name = last_name_Val
            custProfile.save(update_fields=["last_name"])
            custProfile.birthday = birthday_Val
            custProfile.save(update_fields=["birthday"])

            shipAddress = None
            if(ShippingAddress.objects.filter(custProfile=custProfile).first() == None):
                shipAddress = ShippingAddress.objects.create(
                    custProfile=custProfile,
                )
            else:
                shipAddress = get_object_or_404(ShippingAddress,custProfile=custProfile)
            shipAddress.Street = StreetS
            shipAddress.save(update_fields=["Street"])
            shipAddress.State = StateS
            shipAddress.save(update_fields=["State"])
            shipAddress.City = CityS
            shipAddress.save(update_fields=["City"])
            shipAddress.Zipcode = ZipcodeS
            shipAddress.save(update_fields=["Zipcode"])

            billAddress = None
            if (BillingAddress.objects.filter(custProfile=custProfile).first() == None):
                billAddress = BillingAddress.objects.create(
                    custProfile=custProfile,
                )
            else:
                billAddress = get_object_or_404(BillingAddress, custProfile=custProfile)

            billAddress.Street = StreetB
            billAddress.save(update_fields=["Street"])
            billAddress.State = StateB
            billAddress.save(update_fields=["State"])
            billAddress.City = CityB
            billAddress.save(update_fields=["City"])
            billAddress.Zipcode = ZipcodeB
            billAddress.save(update_fields=["Zipcode"])

            creditCard = None
            if(CreditCard.objects.filter(custProfile=custProfile).first() == None):
                creditCard = CreditCard.objects.create(
                    custProfile=custProfile
                )
            else:
                creditCard = get_object_or_404(CreditCard, custProfile=custProfile)

            creditCard.CreditCardNumber = number_Val
            creditCard.save(update_fields=["CreditCardNumber"])
            creditCard.SecurityCode = securityCode_Val
            creditCard.save(update_fields=["SecurityCode"])

            creditCard.ExpMonth = month_Val
            creditCard.save(update_fields=["ExpMonth"])
            creditCard.ExpYear = year_Val
            creditCard.save(update_fields=["ExpYear"])






           # try:
            #   CustomerProfile.objects.update(
             #       first_name = first_name_Val,
              #      last_name = last_name_Val,
                #    email = email_Val,
                 #   password = password_Val,
                  #  username = email_Val

               # )
            #except ValueError:
             #   print(ValueError)
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:

        if (CustomerProfile.objects.filter(user=request.user).first() != None):
            custProfile = get_object_or_404(CustomerProfile, user=request.user)
            fname = custProfile.first_name
            lname = custProfile.last_name
            bdate = custProfile.birthday
            form1 = CustomerProfileForm(initial={'first_name': fname, 'last_name':lname, 'birthday':bdate})

            if (ShippingAddress.objects.filter(custProfile=custProfile).first() != None):
                shipAddress = get_object_or_404(ShippingAddress, custProfile=custProfile)
                stre = shipAddress.Street
                cty = shipAddress.City
                zip = shipAddress.Zipcode
                stat = shipAddress.State
                form2 = ShippingAddressForm(initial={'street': stre, 'city':cty, 'state':stat, 'zipcode':zip})
            else:
                form2 = ShippingAddressForm()

            if (CreditCard.objects.filter(custProfile=custProfile).first() != None):
                creditCard = get_object_or_404(CreditCard, custProfile=custProfile)
                number = creditCard.CreditCardNumber
                code = creditCard.SecurityCode
                month = creditCard.ExpMonth
                year = creditCard.ExpYear
                form3 = CreditCardForm(initial={'number': number, 'securityCode':code, 'month':month, 'year':year})
            else:
                form3 = CreditCardForm()

            if(BillingAddress.objects.filter(custProfile=custProfile).first() != None):
                billingAddress = get_object_or_404(BillingAddress, custProfile=custProfile)
                street = billingAddress.Street
                city = billingAddress.City
                state = billingAddress.State
                zipcode = billingAddress.Zipcode
                form4 = BillingAddressForm(initial={'streetB': street, 'cityB':city, 'stateB': state, 'zipcodeB':zipcode})
            else:
                form4 = BillingAddressForm()
        else:
            form1 = CustomerProfile()
            form2 = ShippingAddressForm()
            form3 = CreditCardForm()
            form4 = BillingAddressForm()

    return render(request, 'Amazon_Core/update_profile.html',  {'form1': form1, 'form2' : form2, 'form3': form3, 'form4': form4  })

def logout_view(request):
    logout(request)
    return render(request, 'Amazon_Core/logout.html')

def catalog(request):
    itemList = Item.objects.all()
    return render(request, 'Amazon_Core/catalog.html', {'itemList': itemList})

def formsetTest(request):
    ShippingFormSet = formset_factory(ShippingAddressForm, extra= 2)
    if(request.method == 'POST'):
        x = 2
    else:
        ship_formSet = ShippingFormSet()
    return render(request, 'Amazon_Core/formsetTest.html', {'ship_formSet':ship_formSet})

def ItemDetail(request,item_id):
    try:
        item = Item.objects.get(pk=item_id)
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = ItemForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                price = form.cleaned_data.get('price')
                numAvailable = form.cleaned_data.get('numAvailable')

                item.price = price
                item.numAvailable = numAvailable
                print(price)
                item.save(update_fields=["price","numAvailable"])
                messages.success(request, 'Info updated successfully.')

        # if a GET (or any other method) we'll create a blank form
        else:
            price = item.price
            numAvailable = item.numAvailable
            form = ItemForm(initial={'price':price, 'numAvailable':numAvailable})


    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'Amazon_Core/detail.html', {'item':item, 'form':form})