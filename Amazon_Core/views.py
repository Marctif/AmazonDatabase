from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, UserLoginForm, CustomerProfileForm, ShippingAddressForm
from .models import Question, demo
from django.http import HttpResponseRedirect
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
                User.objects.create(
                    first_name = first_name_Val,
                    last_name = last_name_Val,
                    email = email_Val,
                    password = password_Val,
                    username = email_Val

                )
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
        form1 = CustomerProfileForm(request.POST)
        form2 = ShippingAddressForm(request.POST)
        # check whether it's valid:
        if form1.is_valid() & form2.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            #first_name_Val= form.cleaned_data.get('first_name')
            #last_name_Val = form.cleaned_data.get('last_name')
            #email_Val = form.cleaned_data.get('email')
            #password_Val = form.cleaned_data.get('password')

            #try:
             #   User.objects.create(
              #      first_name = first_name_Val,
               #     last_name = last_name_Val,
                #    email = email_Val,
                 #   password = password_Val,
                  #  username = email_Val

               # )
            #except ValueError:
             #   print(ValueError)
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = CustomerProfileForm()
        form2 = ShippingAddressForm

    return render(request, 'Amazon_Core/update_profile.html',  {'form1': form1, 'form2' : form2 })

def logout_view(request):
    logout(request)
    return render(request, 'Amazon_Core/logout.html')