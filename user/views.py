from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth# Create your views here.

def login(request):
    if request.method =="POST":
        ##che  if the user exist withthe pass
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect("/employee_admin")
        else:
            return render(request, 'user/login.html', {'error':"Invalid Login Credentials"})
    else:
        return render(request, 'user/login.html')