from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login as auth_login
from django.contrib.auth.models import User
from .models import Userdetails

def registerview(request):
    if request.method=='POST':
        name=request.POST['fullname']
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        if password==cpassword:
            ok=User.objects.create_user(first_name=name,username=username,email=email,password=password)
            sk=Userdetails.objects.create(uuser=ok,phone=phone)
            k=ok.save()
            if k:
                sk.save()
                return redirect('login')

    return render(request,'register.html')

def loginview(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('mainview')
    return render(request,'login.html')

def logoutview(request):
    logout(request)
    return render(request,'index.html')