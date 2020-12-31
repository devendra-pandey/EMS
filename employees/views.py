from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from .models import Employee , Salary ,Sallary_increament ,Monthly_Salary
from client.models import Client , Enquiry , Followup , Company_Profile , Extra_Expenses , Tax
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import EmployeeForm , SallaryForm , Increment_sallaryForm , Sallary_increasesForm , Monthly_SalaryForm
from user.models import User
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Q


@login_required(login_url='/')
def employee_admin(request):
    now = datetime.datetime.now()
    enq_count = Enquiry.objects.all().count()
    emp_count = Employee.objects.all().count()
    client_count = Client.objects.all().count()
    user_count = User.objects.all().count()
    
    context = {
                'emp_count': emp_count,
                'enq_count':enq_count,
                'client_count':client_count,
                'user_count':user_count,
            }
    return render(request, 'employees/dashboard.html',context)

@login_required(login_url='/')
def employees(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(mobile_number__icontains=query) | Q(aadhar__icontains=query)

            emp_info = Employee.objects.all().filter(lookups).distinct()

            paginator = Paginator(emp_info, 2)
            page_number = request.GET.get('page')
            emp_pagination = paginator.get_page(page_number)

            context={
                    'emp_info12': emp_pagination,
                    'submitbutton': submitbutton,
            }                          
            return render(request, 'employees/employees.html', context)
        else:
            emp = Employee.objects.filter(status = '1').order_by('-created')
            ##employee Pagination
            paginator = Paginator(emp, 2)
            page_number = request.GET.get('page')
            emp_pagination = paginator.get_page(page_number)

            context = {
                        'emp_info':emp_pagination,
                    }
            return render(request, 'employees/employees.html',context)

    elif request.method == 'POST':
        datefrom = request.POST['datef']
        dateto = request.POST['datet']

        print(datefrom)
        print(dateto)
        
        emp_info12 = Employee.objects.all().filter( start_date__lte=dateto,start_date__gte =datefrom)

        paginator = Paginator(emp_info12, 2)
        page_number = request.GET.get('page')
        emp_pagination = paginator.get_page(page_number)

        Context = {
            'emp_info':emp_pagination,
        }

        return render(request, 'employees/employees.html', Context)
    else:
        emp = Employee.objects.filter(status = '1').order_by('-created')
        ##employee Pagination
        paginator = Paginator(emp, 2)
        page_number = request.GET.get('page')
        emp_pagination = paginator.get_page(page_number)

        context = {
                    'emp_info':emp_pagination,
                }
        return render(request, 'employees/employees.html',context)



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
            return redirect('employees')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'employees'}}">reload</a>""")
    else:
        return render(request, 'employees/employee_create.html', {'upload_form':form, 'upload_form1':form1 }) 
    

@login_required(login_url='/')
def update_employee(request, id):
    emp_id = int(id)
    try:
        emp_get = Employee.objects.get(id = emp_id)
        sal_get = Salary.objects.get(employe_name= emp_id)
    except Employee.DoesNotExist:
        return redirect('employees')
    form = EmployeeForm(request.POST or None, instance = emp_get)
    form1 = SallaryForm(request.POST or None, instance = sal_get)
    if form.is_valid() and form1.is_valid():
       form.save()
       form1.save()
       return redirect('employees')
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
        return redirect('employees')
    emp_data.status = '0'
    emp_data.save()
    return redirect('employees')

@login_required(login_url='/')
def all_sal(request):
    mon_sal = Monthly_Salary.objects.filter(employee_name__status='1', status='1').order_by('-created')
    ##employee Sallary Pagination
    paginator = Paginator(mon_sal, 2)
    page_number = request.GET.get('page')
    mon_sal_obj = paginator.get_page(page_number)

    context = {
        'mon_sal_obj':mon_sal_obj,
        
    }
    return render(request,'employees/all_sallary.html', context)

@login_required(login_url='/')
def all_sal_increment(request):
    inc_sal = Sallary_increament.objects.filter(employe_name__status='1',status ='1').order_by('-created')

    ##salary increment Pagination
    paginator = Paginator(inc_sal, 2) 
    page_number = request.GET.get('page')
    inc_Sallary_page = paginator.get_page(page_number)


    context = {
        'inc_Sallary_page':inc_Sallary_page,

    }
    return render(request,'employees/all_increment.html', context)

@login_required(login_url='/')
def view_tax(request):
    tax_pro = Tax.objects.filter(status='1').order_by('-created')

    ## Pagination for Tax
    paginator = Paginator(tax_pro, 2)
    page_number = request.GET.get('page')
    page_tax = paginator.get_page(page_number)

    
    context = {
        'page_tax':page_tax,

    }
    return render(request,'employees/view_tax.html', context)

@login_required(login_url='/')
def view_company(request):
    company_pro = Company_Profile.objects.filter(status='1').order_by('-created')


## Pagination for company
    paginator = Paginator(company_pro, 2)
    page_number = request.GET.get('page')
    page_company = paginator.get_page(page_number)

    
    context = {
        'page_company':page_company,

    }
    return render(request,'employees/view_company.html', context)



@login_required(login_url='/')
def view_extra_expenses(request):
    expenses_pro = Extra_Expenses.objects.filter(status ='1').order_by('-created')

    ## Pagination for Expenses
    paginator = Paginator(expenses_pro, 2)
    page_number = request.GET.get('page')
    page_expenses = paginator.get_page(page_number)

    context = {
        'page_expenses':page_expenses,

    }
    return render(request,'employees/view_extra_expenses.html', context)


@login_required(login_url='/')
def view_extra_monthly_expenses(request):
    months = Extra_Expenses.objects.dates('date','month')
    expenses1 = Extra_Expenses.objects.all().filter(status='1').values()
    amount = {}
    for expense in expenses1:
        month = expense['date'].month
        print(month)
        if month in amount:
            amount[month] = amount[month] + expense['expense_amount']
        else:
            amount[month] = expense['expense_amount']
    
    context = {
            'months': months, 
            'amount': amount,
    }
    return render(request,'employees/extra_monthly_expenses.html', context)



@login_required(login_url='/')
def view_extra_yearly_expenses(request):
    years = Extra_Expenses.objects.dates('date','year')
    expenses = Extra_Expenses.objects.all().filter(status='1').values()
    amounts = {}

    for expense in expenses:
        year = expense['date'].year
        if year in amounts:
            amounts[year] = amounts[year] + expense['expense_amount']
        else:
            amounts[year] = expense['expense_amount']
    
    context = {
        'years': years, 
        'amounts': amounts,
              
    }
    return render(request,'employees/extra_yearly_expenses.html', context)



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
            return redirect('all_inc_sallary')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'all_inc_sallary'}}">reload</a>""")
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
        return redirect('all_inc_sallary')
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
        return redirect('all_inc_sallary')
    return render(request, 'employees/increased_sallary.html', {'upload_form':form})


def delete_inc_sal(request, id):
    sal_inc = int(id)
    try:
        sal_inc_data = Sallary_increament.objects.get(id = sal_inc)
        main_id = sal_inc_data.employe_name
        ab = sal_inc_data.hike_sallary
    except Sallary_increament.DoesNotExist:
        return redirect('all_inc_sallary')
    sal_update = Salary.objects.filter(employe_name=main_id)
    for sal_inc in sal_update:
        f_sal = sal_inc.finall_sallary
        print(f_sal)
    to_update = Salary.objects.filter(employe_name=main_id).update(finall_sallary=f_sal - ab)
    sal_inc_data.status = '0'
    sal_inc_data.save()
    return redirect('all_inc_sallary')

@login_required(login_url='/')
def all_monthly_sallary(request):

    months = Monthly_Salary.objects.dates('date','month')
    sallary = Monthly_Salary.objects.all().filter(status='1').values()
    amount = {}
    for expense in sallary:
        month = expense['date'].month
        print(month)
        if month in amount:
            print("hello")
            amount[month] = amount[month] + expense['total_salary']
            print(amount)
        else:
            amount[month] = expense['total_salary']

##monthly pagination of sallary
    paginator = Paginator(months, 2)
    page_number = request.GET.get('page')
    monthly = paginator.get_page(page_number)  

    context = {
        'months':months,
        'amount': amount,
        'sallary':sallary,
        'monthly':monthly,

    }
    return render(request,'employees/monthly_total_sal.html', context)


@login_required(login_url='/')
def monthly_sal(request):
    form = Monthly_SalaryForm()
    if request.method == 'POST':
        form = Monthly_SalaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_sallary')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'all_sallary'}}">reload</a>""")
    else:
        return render(request, 'employees/monthly_sallary.html', {'upload_form':form})


@login_required(login_url='/')
def update_monthly_sal(request, id):
    month_sal_id = int(id)
    try:
        sal_get = Monthly_Salary.objects.get(id = month_sal_id)
    except Monthly_Salary.DoesNotExist:
        return redirect('all_sallary')
    form = Monthly_SalaryForm(request.POST or None, instance = sal_get)
    if form.is_valid():
       form.save()
       return redirect('all_sallary')
    return render(request, 'employees/monthly_sallary.html', {'upload_form':form})

@login_required(login_url='/')
def delete_monthly_sal(request, id):
    monthly_sal_id = int(id)
    try:
        month_Sal = Monthly_Salary.objects.get(id = monthly_sal_id)
    except Monthly_Salary.DoesNotExist:
        return redirect('all_sallary')
    month_Sal.status = '0'
    month_Sal.save()
    return redirect('all_sallary')

