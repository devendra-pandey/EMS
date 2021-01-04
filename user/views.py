from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth# Create your views here.
from django.contrib.auth import logout
from django.contrib import messages

# def login(request):
#     if request.method =="POST":
#         ##che  if the user exist withthe pass
#         uname = request.POST['username']
#         pwd = request.POST['password']
#         user = auth.authenticate(username=uname,password=pwd)
#         if user.is_admin is not None:
#             auth.login(request, user)
#             return redirect("/employee_admin")
#         else:
#             return render(request, 'user/login.html', {'error':"Invalid Login Credentials"})
#     else:
#         return render(request, 'user/login.html')


def login(request):
    if request.method == 'POST':

        #AuthenticationForm_can_also_be_used__

        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = auth.authenticate(request, username=uname, password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect("/employee_admin")
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')

    return render(request, 'user/login.html')





def logout_request(request):
    logout(request)
    return redirect("/")