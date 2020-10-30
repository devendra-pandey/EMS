from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from .models import Employee , Salary ,Sallary_increament ,Monthly_Salary
from client.models import Client , Enquiry
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import EmployeeForm , SallaryForm , Increment_sallaryForm , Sallary_increasesForm , Monthly_SalaryForm
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
    enq = Enquiry.objects.all().filter(status = '1')
    emp = Employee.objects.filter(status = '1').order_by('-created')
    client = Client.objects.all().filter(status = '1')
    inc_sal = Sallary_increament.objects.all()
    mon_sal = Monthly_Salary.objects.all().order_by('-created')
    
##employee Pagination
    page = request.GET.get('page',1)
    paginator = Paginator(emp , 2)
    print("******")
    print(paginator)
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
                'inc_sal':inc_sal,
                'mon_sal':mon_sal,
                
            }
    return render(request, 'employees/dashboard.html',context)


@login_required
def employee_create(request):  
    form = EmployeeForm()
    form1 = SallaryForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        form1 = SallaryForm(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            obj = form.save()
            choice = form1.save(commit=False)
            choice.employee_name = obj
            choice.save()
            return redirect('dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dashboard'}}">reload</a>""")
    else:
        return render(request, 'employees/employee_create.html', {'upload_form':form, 'upload_form1':form1 }) 
    

def update_employee(request, id):
    emp_id = int(id)
    try:
        emp_get = Employee.objects.get(id = emp_id)
        sal_get = Salary.objects.get(employee_name= emp_id)
    except Employee.DoesNotExist:
        return redirect('dashboard')
    form = EmployeeForm(request.POST or None, instance = emp_get)
    form1 = SallaryForm(request.POST or None, instance = sal_get)
    if form.is_valid() and form1.is_valid():
       form.save()
       form1.save()
       return redirect('dashboard')
    return render(request, 'employees/employee_create.html', {'upload_form':form, 'upload_form1':form1 })


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
    return render(request, 'employees/info_emp_client.html', context)

def delete_emp(request, id):
    emp_id = int(id)
    try:
        emp_data = Employee.objects.get(id = emp_id)
    except Employee.DoesNotExist:
        return redirect('dashboard')
    emp_data.status = '0'
    emp_data.save()
    return redirect('dashboard')

def sallary_increment_create(request):  
    form = Increment_sallaryForm()
    if request.method == 'POST':
        form = Increment_sallaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dashboard'}}">reload</a>""")
    else:
        return render(request, 'employees/increased_sallary.html', {'upload_form':form})

def update_inc_sal(request, id):
    inc_sal_id = int(id)
    try:
        inc_sal_get = Sallary_increament.objects.get(id = inc_sal_id)
    except Sallary_increament.DoesNotExist:
        return redirect('dashboard')
    form = Increment_sallaryForm(request.POST or None, instance = inc_sal_get)
    if form.is_valid():
       form.save()
       return redirect('dashboard')
    return render(request, 'employees/increased_sallary.html', {'upload_form':form})




def monthly_sal(request):
    form = Monthly_SalaryForm()
    if request.method == 'POST':
        form = Monthly_SalaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dashboard'}}">reload</a>""")
    else:
        return render(request, 'employees/monthly_sallary.html', {'upload_form':form})

def update_monthly_sal(request, id):
    month_sal_id = int(id)
    try:
        sal_get = Monthly_Salary.objects.get(id = month_sal_id)
    except Monthly_Salary.DoesNotExist:
        return redirect('dashboard')
    form = Monthly_SalaryForm(request.POST or None, instance = sal_get)
    if form.is_valid():
       form.save()
       return redirect('dashboard')
    return render(request, 'employees/monthly_sallary.html', {'upload_form':form})
