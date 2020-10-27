from django.shortcuts import render, redirect

def employee_admin(request):
    return render(request, 'employees/dashboard.html')