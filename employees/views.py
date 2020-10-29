from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from .models import Employee , Salary ,Sallary_increament
from client.models import Client
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import EmployeeForm
from user.models import User
from django.contrib.auth.decorators import login_required


@login_required
def employee_create(request):  
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.save()
            return redirect('dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dashboard'}}">reload</a>""")
    else:
        return render(request, 'employees/employee_create.html', {'upload_form':form}) 
    

@login_required
def employee_admin(request):
    emp_count = Employee.objects.all().count()
    print(emp_count) 
    client_count = Client.objects.all().count()
    user_count = User.objects.all().count()
    emp = Employee.objects.filter(status = 'Active')
    client = Client.objects.all()

    paginator = Paginator(emp, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        employee_all = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        employee_all = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        employee_all = paginator.page(paginator.num_pages)

    context = {
                'emp_count': emp_count,
                'employee_all':employee_all,
                'client_count':client_count,
                'user_count':user_count,
                'emp': emp,
                'client':client,
                
            }
    return render(request, 'employees/dashboard.html',context)

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