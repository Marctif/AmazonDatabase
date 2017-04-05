from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import  CustomerProfileForm, ShippingAddressForm, CreditCardForm, BillingAddressForm, ItemForm
from .models import CustomerProfile, ShippingAddress, CreditCard, BillingAddress, MONTHS, YEARS, Item
from .forms import CustomerProfileForm, ShippingAddressForm, CreditCardForm, BillingAddressForm
from .models import CustomerProfile, ShippingAddress, CreditCard, BillingAddress, MONTHS, YEARS
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
#from django.core.context_processors import csrf
from django.template import RequestContext  # For CSRF
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.

def home(request):
    now = datetime.datetime.now()
    hour = now.hour
    print(datetime.datetime.now())
    print(hour)
    return render(request, 'Amazon_Core/home.html')

def demo(request):
    return render(request, 'Amazon_Core/demo.html')

@login_required
def userprofile(request):
    user = request.user
    try:
        profile = CustomerProfile.objects.get(user = request.user)
    except:
        profile = CustomerProfile.objects.create(user = request.user)
        CreditCard.objects.create(custProfile=profile, CreditCardNumber=0000000000000000)
    shipping = profile.shippingaddress_set.all()
    billing = profile.billingaddress_set.all()
    credit = profile.creditcard_set.all()
    context = {'user': user, 'profile':profile, 'shipping': shipping, 'billing': billing, 'credit': credit}
    template = 'Amazon_Core/profile.html'
    return render(request,template,context)

@login_required
def user_edit(request):

    if request.method == 'POST':
        profile_form = CustomerProfileForm(request.POST, instance=request.user.CustomerProfile)
        shipping_form = ShippingAddressForm(request.POST, instancel=request.user.CustomerProfile.ShippingAddress)

        if all([profile_form.is_valid(), shipping_form.is_valid()]):
            profile = profile_form.save()
            shipping = shipping_form.save()
            return HttpResponseRedirect('/profile/')

    else:
        profile_form = CustomerProfileForm(instance=request.user.CustomerProfile)
        shipping_form = ShippingAddressForm(instance=request.user.CustomerProfile.ShippingAddress)

    return render(request, 'Amazon_Core/edit.html', {
        'profile_form': profile_form,
        'shipping_form': shipping_form,
    })

def update_profile(request):
    return render(request, 'Amazon_Core/update_profile.html')

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

def track(request):
    itemList = Item.objects.all()
    return render(request, 'Amazon_Core/track.html') , {'itemList': itemList}


def formsetTest(request):
    ShippingFormSet = formset_factory(ShippingAddressForm, extra= 2)
    if(request.method == 'POST'):

        ship_formSet = ShippingFormSet(request.POST)
        if ship_formSet.is_valid():
            for shipForm in ship_formSet:
                street = shipForm.cleaned_data.get('street')
                print(street)
    else:
        ship_formSet = ShippingFormSet()
    return render(request, 'Amazon_Core/formsetTest.html', {'ship_formSet':ship_formSet})

def ItemDetail(request,item_id):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/catalog/')
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
                item.save()
                messages.success(request, 'Info updated successfully.')
                return HttpResponseRedirect('/catalog/')

        # if a GET (or any other method) we'll create a blank form
        else:
            price = item.price
            numAvailable = item.numAvailable
            form = ItemForm(initial={'price':price, 'numAvailable':numAvailable})


    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'Amazon_Core/detail.html', {'item':item, 'form':form})

def orderDetail(request, order_id):
    order = get_object_or_404(Order,id=order_id)
    shipmentSet = Shipment.objects.filter(order=order)

    if(request.method == 'POST'):
        returns = False
        for ship in shipmentSet:
            status = request.POST.get(str(ship.litem.id))
            if(status == 'on'):
                ship.status = 'RI'
                ship.save()
                order.save()
                returns = True
        if(returns):
            messages.success(request, 'Returns initiated successfully.')

    return render(request, 'Amazon_Core/orderDetail.html',{'order':order, 'shipmentSet': shipmentSet})

def dynamicShipping(request):
    # This class is used to make empty formset forms required
    # See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False
    custProfile = get_object_or_404(CustomerProfile, user=request.user)
    ShipFormSet = formset_factory(ShippingForm, max_num=10, formset=RequiredFormSet)
    ShipSet = ShippingAddress.objects.filter(custProfile=custProfile)

    if request.method == 'POST':  # If the form has been submitted...
        # todo_list_form = TodoListForm(request.POST)  # A form bound to the POST data
        # Create a formset from the submitted data
        ship_formset = ShipFormSet(request.POST, request.FILES)

        # drop all current Addresses
        ShipSet.delete()
        x = 1
        if  ship_formset.is_valid():
            for form in ship_formset.forms:
                ship_item = form.save(commit=False)

                #Re add all Addresses
                ShippingAddress.objects.create(
                    custProfile=custProfile,
                    Street=ship_item.Street,
                    City=ship_item.City,
                    State=ship_item.State,
                    Zipcode=ship_item.Zipcode,
                    count=x
                )
                x = x + 1
            messages.success(request, 'Addresses updated successfully.')
            return HttpResponseRedirect('/profile/')  # Redirect to a 'success' page
    else:
            ship_formset = ShipFormSet(initial=[
     {'Street': x.Street, 'City' : x.City, 'State' : x.State, 'Zipcode' : x.Zipcode
      } for x in ShipSet])

    c = {
         'todo_item_formset': ship_formset,
         }
    #c.update(csrf(request))

    return render(request, 'Amazon_Core/dynamicShipping.html', c)

def dynamicBilling(request):
    # This class is used to make empty formset forms required
    # See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False
    custProfile = get_object_or_404(CustomerProfile, user=request.user)
    BillFormSet = formset_factory(BillingForm, max_num=10, formset=RequiredFormSet)
    BillSet = BillingAddress.objects.filter(custProfile=custProfile)

    if request.method == 'POST':  # If the form has been submitted...
        # todo_list_form = TodoListForm(request.POST)  # A form bound to the POST data
        # Create a formset from the submitted data
        bill_formset = BillFormSet(request.POST, request.FILES)

        # drop all current Addresses
        BillSet.delete()
        x = 1
        if  bill_formset.is_valid():
            for form in bill_formset.forms:
                bill_item = form.save(commit=False)

                #Re add all Addresses
                BillingAddress.objects.create(
                    custProfile=custProfile,
                    Street=bill_item.Street,
                    City=bill_item.City,
                    State=bill_item.State,
                    Zipcode=bill_item.Zipcode,
                    count=x
                )
                x = x + 1
            messages.success(request, 'Addresses updated successfully.')
            return HttpResponseRedirect('/profile/')  # Redirect to a 'success' page
    else:
            bill_formset = BillFormSet(initial=[
     {'Street': x.Street, 'City' : x.City, 'State' : x.State, 'Zipcode' : x.Zipcode
      } for x in BillSet])

    c = {
         'todo_item_formset': bill_formset,
         }
    #c.update(csrf(request))

    return render(request, 'Amazon_Core/dynamicBilling.html', c)

def cart(request):
    items = Item.objects.all()
    return render(request, 'Amazon_Core/cart.html',{'items':items})


@csrf_exempt
def checkout(request):
    if(request.method == 'POST'):

        custProfile = get_object_or_404(CustomerProfile, user=request.user)

        form = OrderForm(custProfile,request.POST)
        if(form.is_valid()):
            latestOrder = Order.objects.latest('id')

            billAdr = form.cleaned_data['billAddress']
            shipAdr = form.cleaned_data['shipAddress']
            creditCard = form.cleaned_data['payMethod']

            latestOrder.billAddress = billAdr
            latestOrder.shipAddress = shipAdr
            latestOrder.payMethod = creditCard



            latestOrder.save()

            messages.success(request, 'Order created successfully.')

            return HttpResponseRedirect('/')

        else:
            items = Item.objects.all()

            itemSet = []
            quantitySet = []
            count = 0

            for x in range(1, items.__sizeof__()):
                name = "item_" + "name" + "_" + str(x)
                quantity = "item_" + "quantity" + "_" + str(x)
                valName = request.POST.get(name)
                valQuantity = request.POST.get(quantity)
                if(valName != None):
                    #print(valName)
                    totalQuantity = 0
                    if (valQuantity != None):
                        totalQuantity = int(valQuantity)
                    item = get_object_or_404(Item, name=valName)
                    item.numAvailable = totalQuantity
                    itemSet.append(item)
                    quantitySet.append(totalQuantity)
                    #print(item.SKU)

            for item in itemSet:
                count = count + 1
            #for q in quantitySet:
            #    print(q)

            lineItemSet = []

            for x in range(0, count):
                print(itemSet[x].name + " " + str(quantitySet[x]))
                item = itemSet[x]
                quantity = quantitySet[x]

                modelItem = get_object_or_404(Item,name=item.name)
                if(quantity > modelItem.numAvailable):
                    messages.error(request, 'You selected too many of item: ' + item.name)
                    return HttpResponseRedirect('/cart/')

                else:
                    modelItem.numAvailable = modelItem.numAvailable - quantity
                    modelItem.save()


                subtotal = item.price * quantity
                lItem = LineItem.objects.create(
                    item=item,
                    quantity=quantity,
                    cost=item.price,
                    subTotal=subtotal
                )
                lineItemSet.append(lItem)


            card = get_object_or_404(CreditCard, custProfile=custProfile)

            order = Order.objects.create(
                custProfile=custProfile,
                status='PE',
                payMethod=card,
                total_cost=0,
            )

            total = 0

            for i in lineItemSet:
                ship = Shipment.objects.create(
                    order=order,
                    litem=i,
                    status='PI',

                )
                total = total + i.quantity * i.cost

            order.total_cost = total * 1.0825

            order.save()



        #print(request.POST.get("item_name_1"))

    else:
        custProfile = get_object_or_404(CustomerProfile, user=request.user)
        form = OrderForm(custProfile=custProfile)
        x = 3

    return render(request, 'Amazon_Core/checkout.html', {'form': form})

def viewOrder(request):
    profile = get_object_or_404(CustomerProfile, user=request.user)
    orderSet = Order.objects.filter(custProfile=profile)

    return render(request, 'Amazon_Core/viewOrder.html', {'orderSet':orderSet})

def editCreditcard(request):
    custProfile = get_object_or_404(CustomerProfile,user=request.user)
    try:
        creditcard = CreditCard.objects.get(custProfile=custProfile)
    except:
        creditcard = CreditCard.objects.create(custProfile=custProfile)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreditCardForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            number = form.cleaned_data.get('number')
            securityCode = form.cleaned_data.get('securityCode')
            month = form.cleaned_data.get('month')
            year = form.cleaned_data.get('year')

            creditcard.CreditCardNumber = number
            creditcard.SecurityCode = securityCode
            creditcard.ExpMonth = month
            creditcard.ExpYear = year

            creditcard.save()

            messages.success(request, 'Credit card info updated successfully.')
            return HttpResponseRedirect('/profile/')

    # if a GET (or any other method) we'll create a blank form
    else:
        number = creditcard.CreditCardNumber
        securityCode = creditcard.SecurityCode
        month = creditcard.ExpMonth
        year = creditcard.ExpYear
        form = CreditCardForm(initial={'number': number, 'securityCode': securityCode,'ExpMonth': month, 'ExpYear':year})

    return render(request,'Amazon_Core/editCreditcard.html', {'form':form})

def createSubscription(request):
    items = Item.objects.all()
    custProfile = get_object_or_404(CustomerProfile, user=request.user)

    if(request.method == 'POST'):
        orderForm = OrderForm(custProfile, request.POST)
        billAdr = BillingAddress.objects.get(pk=orderForm['billAddress'].value())
        shipAdr = ShippingAddress.objects.get(pk=orderForm['shipAddress'].value())
        creditCard = CreditCard.objects.get(pk=orderForm['payMethod'].value())

        timeForm = TimeframeForm(request.POST)
        period = timeForm['period'].value()
        timeframe = Timeframe.objects.create(period=period)

        subscription = Subscription.objects.create(custProfile=custProfile,timeframe=timeframe,billAddress=billAdr,
                                                   shipAddress=shipAdr,payMethod=creditCard,total_cost=0)

        subitemset = []
        for item in items:
            val = request.POST.get(str(item.id))
            if(val != ""):
                print(item.name + " " + str(item.price) + " " + val)
                subtotal = int(val) * item.price
                subitem = SubscriptionItem.objects.create(subscription=subscription,item=item,cost=item.price, quantity=int(val), subTotal=subtotal)
                subitemset.append(subitem)

        subscription.save()

        messages.success(request, 'Subscription created successfully.')
        return HttpResponseRedirect('/')




    else:
        orderForm = OrderForm(custProfile=custProfile)
        timeForm = TimeframeForm()
    return render(request,'Amazon_Core/createSubscriptions.html',{'items': items,'form':orderForm,'form2':timeForm})

def viewSubscriptions(request):

    profile = get_object_or_404(CustomerProfile, user=request.user)
    subscriptions = Subscription.objects.filter(custProfile=profile)

    if (request.method == 'POST'):
        delete = False
        for sub in subscriptions:
            status = request.POST.get(str(sub.id))
            if (status == 'on'):
                sub.delete()
                delete = True
        if(delete):
            messages.success(request, 'Templates deleted successfully.')
            return HttpResponseRedirect('/')


    return render(request,'Amazon_Core/viewSubscriptions.html',{'subscriptions':subscriptions})

def subscriptionDetail(request, subscription_id):
    subscription = get_object_or_404(Subscription,id=subscription_id)
    subItemSet = SubscriptionItem.objects.filter(subscription=subscription)

    if(request.method == 'POST'):
        for sub in subItemSet:
           status = request.POST.get(str(sub.id))
           if(status == 'on'):
               sub.delete()
           else:
                amount = request.POST.get(str(sub.id)+"q")
                sub.quantity = int(amount)

                sub.subTotal = int(amount) * int(sub.cost)
                sub.save()

        subscription.save()
        messages.success(request, 'Template changed successfully.')
        return HttpResponseRedirect('/viewSubscriptions/')

    return render(request, 'Amazon_Core/subscriptionDetail.html',{'subscription':subscription, 'subItemSet': subItemSet})

def addSubItem(request, subId):
    subscription = get_object_or_404(Subscription,id=subId)

    if(request.method == 'POST'):
        form = SubForm(request.POST)
        if(form.is_valid()):
            item = form.cleaned_data.get('item')
            amount = form.cleaned_data.get('amount')
            subitem = SubscriptionItem.objects.create(subscription=subscription, item=item, cost=item.price,
                                                      quantity=amount, subTotal=(amount * item.price))
            messages.success(request, 'Item added to template.')
            return HttpResponseRedirect('/viewSubscriptions/' + str(subId))

    else:
        form = SubForm()
    return  render(request,'Amazon_Core/addSubItem.html',{'form':form})