from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from .models import Employee , Salary ,Sallary_increament ,Monthly_Salary
from client.models import Client , Enquiry , Followup
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import EmployeeForm , SallaryForm , Increment_sallaryForm , Sallary_increasesForm , Monthly_SalaryForm
from user.models import User
from django.contrib.auth.decorators import login_required
import datetime



@login_required(login_url='/')
def employee_admin(request):
    now = datetime.datetime.now()
    enq_count = Enquiry.objects.all().count()
    emp_count = Employee.objects.all().count()
    client_count = Client.objects.all().count()
    user_count = User.objects.all().count()
    enq = Enquiry.objects.all().filter(status = '1').order_by('-created')
    emp = Employee.objects.filter(status = '1').order_by('-created')
    client = Client.objects.all().filter(status = '1').order_by('-created')
    inc_sal = Sallary_increament.objects.filter(employe_name__status='1',status ='1').order_by('-created')
    mon_sal = Monthly_Salary.objects.filter(employee_name__status='1', status='1').order_by('-created')
    feedback = Followup.objects.filter(status='1').order_by('-created')
    
##employee Pagination
    paginator = Paginator(emp, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

##employee Sallary Pagination
    paginator = Paginator(mon_sal, 2)
    page_number = request.GET.get('page')
    mon_sal_obj = paginator.get_page(page_number)

##salary increment Pagination
    paginator = Paginator(inc_sal, 2) 
    page_number = request.GET.get('page')
    inc_Sallary_page = paginator.get_page(page_number)

##client pagination
    paginator = Paginator(client, 2) 
    page = request.GET.get('page')
    try:
        client_all = paginator.page(page)
    except PageNotAnInteger:
        client_all = paginator.page(1)
    except EmptyPage:
        client_all = paginator.page(paginator.num_pages)

    context = {
                'emp_count': emp_count,
                'enq_count':enq_count,
                'page_obj':page_obj,
                'inc_Sallary_page':inc_Sallary_page,
                'client_all':client_all,
                'client_count':client_count,
                'user_count':user_count,
                'client':client,
                'mon_sal_obj':mon_sal_obj,
                
            }
    return render(request, 'employees/dashboard.html',context)


@login_required(login_url='/')
def enquiry_admin(request):
    now = datetime.datetime.now()
    enq = Enquiry.objects.all().filter(status = '1').order_by('-created')
    feedback = Followup.objects.filter(status='1').order_by('-created')

##FeedBack Pagination
    paginator = Paginator(feedback, 2)
    page_number = request.GET.get('page')
    feedback_obj = paginator.get_page(page_number)

##Enquiry Pagination
    paginator = Paginator(enq, 2) 
    page = request.GET.get('page')
    try:
        enq_all = paginator.page(page)
    except PageNotAnInteger:
        enq_all = paginator.page(1)
    except EmptyPage:
        enq_all = paginator.page(paginator.num_pages)
    
    context = {
                'enq_all':enq_all,
                'feedback_obj':feedback_obj,
                
            }
    return render(request, 'employees/enquiry_dashboard.html',context)



@login_required(login_url='/')
def employee_create(request):  
    form = EmployeeForm()
    form1 = SallaryForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        form1 = SallaryForm(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            obj = form.save()
            choice = form1.save(commit=False)
            choice.employe_name_id = obj.id
            choice.save()
            return redirect('dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dashboard'}}">reload</a>""")
    else:
        return render(request, 'employees/employee_create.html', {'upload_form':form, 'upload_form1':form1 }) 
    

@login_required(login_url='/')
def update_employee(request, id):
    emp_id = int(id)
    try:
        emp_get = Employee.objects.get(id = emp_id)
        sal_get = Salary.objects.get(employe_name= emp_id)
    except Employee.DoesNotExist:
        return redirect('dashboard')
    form = EmployeeForm(request.POST or None, instance = emp_get)
    form1 = SallaryForm(request.POST or None, instance = sal_get)
    if form.is_valid() and form1.is_valid():
       form.save()
       form1.save()
       return redirect('dashboard')
    return render(request, 'employees/employee_create.html', {'upload_form':form, 'upload_form1':form1 })

@login_required(login_url='/')
def info(request,id):
    emp_info = get_object_or_404(Employee , id=id)
    print("********")
    print(emp_info)
    sallary_info = get_object_or_404(Salary , employe_name = id)
    print("****")
    print(sallary_info)

    context = {
        'emp_info':emp_info,
        'sallary_info':sallary_info,
    }
    return render(request, 'employees/info_emp_client.html', context)

@login_required(login_url='/')
def delete_emp(request, id):
    emp_id = int(id)
    try:
        emp_data = Employee.objects.get(id = emp_id)
    except Employee.DoesNotExist:
        return redirect('dashboard')
    emp_data.status = '0'
    emp_data.save()
    return redirect('dashboard')


@login_required(login_url='/')
def sallary_increment_create(request):  
    form = Increment_sallaryForm()
    if request.method == 'POST':
        form = Increment_sallaryForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            id = obj.employe_name
            emp_increased_sal = obj.hike_sallary
            print("*** hey")
            print(id)
            ab = Salary.objects.filter(employe_name=id)
            print(ab)
            for fs in ab:
                final_sallary1 = fs.finall_sallary

            to_update = Salary.objects.filter(employe_name=id).update(incresed_sallary=emp_increased_sal, finall_sallary= final_sallary1 + emp_increased_sal )
            print("done")
            return redirect('dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dashboard'}}">reload</a>""")
    else:
        return render(request, 'employees/increased_sallary.html', {'upload_form':form})
   
@login_required(login_url='/')
def update_inc_sal(request, id):
    inc_sal_id = int(id)
    try:
        inc_sal_get = Sallary_increament.objects.get(id = inc_sal_id)
        ab = inc_sal_get.hike_sallary
        print(ab)
    except Sallary_increament.DoesNotExist:
        return redirect('dashboard')
    form = Increment_sallaryForm(request.POST or None, instance = inc_sal_get)
    if form.is_valid():
        obj = form.save()
        id = obj.employe_name
        emp_increased_sal = obj.hike_sallary
        sal_update = Salary.objects.filter(employe_name=id)
        for sal_inc in sal_update:
            f_sal = sal_inc.finall_sallary
            print(f_sal)
        print("*** hey")
        print(id)
        to_update = Salary.objects.filter(employe_name=id).update(incresed_sallary=emp_increased_sal,finall_sallary=f_sal + emp_increased_sal - ab)
        print("done")
        return redirect('dashboard')
    return render(request, 'employees/increased_sallary.html', {'upload_form':form})


def delete_inc_sal(request, id):
    sal_inc = int(id)
    try:
        sal_inc_data = Sallary_increament.objects.get(id = sal_inc)
        main_id = sal_inc_data.employe_name
        ab = sal_inc_data.hike_sallary
    except Sallary_increament.DoesNotExist:
        return redirect('dashboard')
    sal_update = Salary.objects.filter(employe_name=main_id)
    for sal_inc in sal_update:
        f_sal = sal_inc.finall_sallary
        print(f_sal)
    to_update = Salary.objects.filter(employe_name=main_id).update(finall_sallary=f_sal - ab)
    sal_inc_data.status = '0'
    sal_inc_data.save()
    return redirect('dashboard')


@login_required(login_url='/')
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


@login_required(login_url='/')
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

@login_required(login_url='/')
def delete_monthly_sal(request, id):
    monthly_sal_id = int(id)
    try:
        month_Sal = Monthly_Salary.objects.get(id = monthly_sal_id)
    except Monthly_Salary.DoesNotExist:
        return redirect('dashboard')
    month_Sal.status = '0'
    month_Sal.save()
    return redirect('dashboard')

