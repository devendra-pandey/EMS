from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from .models import Employee , Salary ,Sallary_increament
from client.models import Client , Enquiry
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import EmployeeForm , SallaryForm
from user.models import User
from django.contrib.auth.decorators import login_required
import datetime



@login_required
def employee_admin(request):
    now = datetime.datetime.now()
    enq_count = Enquiry.objects.all().count()
    emp_count = Employee.objects.all().count()
    client_count = Client.objects.all().count()
    user_count = User.objects.all().count()
    enq = Enquiry.objects.all()
    emp = Employee.objects.filter(status = 'Active')
    client = Client.objects.all()
    
##employee Pagination
    page = request.GET.get('page',1)
    paginator = Paginator(emp, 2)
    try:
        employee_all = paginator.page(page)
    except PageNotAnInteger:
        employee_all = paginator.page(1)
    except EmptyPage:
        employee_all = paginator.page(paginator.num_pages)

##client pagination
    paginator = Paginator(client, 5) 
    page = request.GET.get('page')
    try:
        client_all = paginator.page(page)
    except PageNotAnInteger:
        client_all = paginator.page(1)
    except EmptyPage:
        client_all = paginator.page(paginator.num_pages)

##Enquiry Pagination
    paginator = Paginator(enq, 5) 
    page = request.GET.get('page')
    try:
        enq_all = paginator.page(page)
    except PageNotAnInteger:
        enq_all = paginator.page(1)
    except EmptyPage:
        enq_all = paginator.page(paginator.num_pages)

    context = {
                'emp_count': emp_count,
                'enq_count':enq_count,
                'enq':enq,
                'now':now,
                'employee_all':employee_all,
                'client_all':client_all,
                'enq_all':enq_all,
                'client_count':client_count,
                'user_count':user_count,
                'emp': emp,
                'client':client,
                
            }
    return render(request, 'employees/dashboard.html',context)




@login_required
def employee_create(request):  
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dashboard'}}">reload</a>""")
    else:
        return render(request, 'employees/employee_create.html', {'upload_form':form}) 
    

def update_employee(request, id):
    emp_id = int(id)
    try:
        emp_get = Employee.objects.get(id = emp_id)
    except Employee.DoesNotExist:
        return redirect('dashboard')
    form = EmployeeForm(request.POST or None, instance = emp_get)
    if form.is_valid():
       form.save()
       return redirect('dashboard')
    return render(request, 'employees/employee_create.html', {'upload_form':form})


def info(request,id):
    emp_info = get_object_or_404(Employee , id=id)
    print("********")
    print(emp_info)
    sallary_info = get_object_or_404(Salary , employee_name = id)
    print("****")
    print(sallary_info)

    context = {
        'emp_info':emp_info,
        'sallary_info':sallary_info,
    }

    # if emp_info:
    #     return redirect ('dashboard')
    # else:
    return render(request, 'employees/info_emp_client.html', context)


def sallary(request):
    form = SallaryForm()
    if request.method == 'POST':
        form = SallaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dashboard'}}">reload</a>""")
    else:
        return render(request , 'employees/sallary.html',{'upload_form':form})