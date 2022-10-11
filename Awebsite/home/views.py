from email import message
import re
from turtle import st
from django.shortcuts import render, redirect, HttpResponse
from home.models import Contacts
from home.models import Signup
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'index.html')

def doctors(request):
    return render(request, 'doctors.html')

def contacts(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email') 
        Address = request.POST.get('Address')
        Phone = request.POST.get('Phone')
        Desc = request.POST.get('Desc')
        contact = Contacts(Name=Name, Email=Email, Address=Address, Phone=Phone, Desc=Desc)
        contact.save()
    return render(request, 'contacts.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        occupation = request.POST['occupation']
        country = request.POST['country']
        city = request.POST['city']
        agree = request.POST['agree']

        #creating user 
        myuser = User.objects.create_user(username=username, email=email, password=password) 
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save() #save user
        messages.success(request, 'Successfully signed up, data saved, >>> Now login <<<')
        return redirect('index')
    else:
        return render(request, 'signup.html')    

def profile(request):
    return render(request, 'profile.html')

def services(request):            
    return render(request, 'services.html')

def logIn(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            #login
            login(request, user)
            messages.success(request, "successfully logged in")
            return redirect('index')
        else:
            #login fail
            messages.error(request, "Error occured while logging in")
            return redirect('index')
    return render(request, 'logIn.html')

def logout(request):
    auth.logout(request)
    messages.error(request, "Successfully logged out")
    return redirect('index')
    
