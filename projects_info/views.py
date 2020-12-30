from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from client.models import Project , Project_income,Project_Assign
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

@login_required(login_url='/')
def proj_info(request, id):
    proj_info = get_object_or_404(Project, id=id)
    context = {
        'proj_info':proj_info
    }
    return render(request, 'projects_info/proj_info.html',context)


@login_required(login_url='/')
def proj_income_details(request):
    proj_inc = Project_income.objects.filter(status='1').order_by('-created')

    ##Paginator of Project Income
    paginator = Paginator(proj_inc, 2)
    page_number = request.GET.get('page')
    proj_inc_page = paginator.get_page(page_number)

    context = {
        'proj_inc_page':proj_inc_page,
    }
    return render(request, 'projects_info/proj_income_details.html',context)


@login_required(login_url='/')
def proj_assign_details(request):
    proj_assign = Project_Assign.objects.filter(status='1', completed='0').order_by('-created')

    ##PAgination for Assign Project
    paginator = Paginator(proj_assign, 2)
    page_number = request.GET.get('page')
    proj_assign_page = paginator.get_page(page_number)

    context = {
        'proj_assign_page':proj_assign_page,
    }
    return render(request, 'projects_info/assign_proj.html',context)

