from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from client.models import Project , Project_income
from employees.models import Employee, Sallary_increament
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

# Create your views here.

@login_required(login_url='/')
def timeline(request):
    return render(request, 'projects_info/timeline.html')

@login_required(login_url='/')
def employee_data(request):
    page_data = 15
    if request.method == 'POST':
        datefrom = request.POST['datef']
        dateto = request.POST['datet']

        print(datefrom)
        print(dateto)
        emp_info = Employee.objects.all().filter( start_date__lte=dateto,start_date__gte =datefrom)

        paginator = Paginator(emp_info, page_data)
        page_number = request.GET.get('page')
        emp_pagination = paginator.get_page(page_number)
        

        Context = {
            'emp_info':emp_pagination,
        }

        return render(request, 'projects_info/employee_data.html', Context)
    else:
        emp_info = Employee.objects.all()

        ##employee
        paginator = Paginator(emp_info, page_data)
        page_number = request.GET.get('page')
        emp_pagination = paginator.get_page(page_number)
   
        Context = {
            'emp_info':emp_pagination,
        }

        return render(request, 'projects_info/employee_data.html', Context)


@login_required(login_url='/')
def data_projects(request):
    page_data = 15
    if request.method == 'POST':
        datefromp = request.POST['datefp']
        datetopr = request.POST['datetp']

        proj_info = Project.objects.all().filter( created__lte=datetopr,created__gte =datefromp)

        paginator = Paginator(proj_info, page_data)
        page_number = request.GET.get('page')
        proj_pagination = paginator.get_page(page_number)

        Context = {
            'proj_info':proj_pagination,
        }
        return render(request, 'projects_info/proj_client.html', Context)
    else:
        proj_info = Project.objects.all()

        ##project
        paginator = Paginator(proj_info, page_data)
        page_number = request.GET.get('page')
        proj_pagination = paginator.get_page(page_number)
    
        Context = {
            'proj_info':proj_pagination,
        }
        return render(request, 'projects_info/proj_client.html', Context)

