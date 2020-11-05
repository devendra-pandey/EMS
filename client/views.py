from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ClientForm , EnquiryForm ,FollowupForm , ProjectForm , Project_incomeForm , Project_AssignForm , Company_ProfileForm , Extra_ExpensesForm , TaxForm , InvoiceForm
from .models import Enquiry ,Followup , Project, Project_income , Project_Assign , Client , Company_Profile , Extra_Expenses , Tax , Invoice
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

@login_required(login_url='/')
def client_create(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dashboard'}}">reload</a>""")
    else:  
        return render(request, 'client/client_create.html', {'upload_form':form})

@login_required(login_url='/')
def update_client(request, id):
    client_id = int(id)
    try:
        client_get = Client.objects.get(id = client_id)
    except Client.DoesNotExist:
        return redirect('dashboard')
    form = ClientForm(request.POST or None, instance = client_get)
    if form.is_valid():
       form.save()
       return redirect('dashboard')
    return render(request, 'client/client_create.html', {'upload_form':form})

@login_required(login_url='/')
def delete_client(request, id):
    client_id = int(id)
    try:
        client_data = Client.objects.get(id = client_id)
    except Client.DoesNotExist:
        return redirect('dashboard')
    client_data.status = '0'
    client_data.save()
    return redirect('dashboard')


@login_required(login_url='/')
def create_enquiry(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dashboard'}}">reload</a>""")
    else:      
        return render(request, 'client/enquiry.html', {'upload_form':form})

@login_required(login_url='/')
def update_enquiry(request, id):
    enquiry_id = int(id)
    try:
        enq_get = Enquiry.objects.get(id = enquiry_id)
    except Enquiry.DoesNotExist:
        return redirect('dashboard')
    form = EnquiryForm(request.POST or None, instance = enq_get)
    if form.is_valid():
       form.save()
       return redirect('dashboard')
    return render(request, 'client/enquiry.html', {'upload_form':form})

@login_required(login_url='/')
def delete_enquiry(request, id):
    enq_id = int(id)
    try:
        enq_data = Enquiry.objects.get(id = enq_id)
    except Enquiry.DoesNotExist:
        return redirect('dashboard')
    enq_data.status = '0'
    enq_data.save()
    return redirect('dashboard')


@login_required(login_url='/')
def create_followup(request):
    form = FollowupForm()
    if request.method == 'POST':
        form = FollowupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dashboard'}}">reload</a>""")
    else:      
        return render(request, 'client/follow_up.html', {'upload_form':form})


@login_required(login_url='/')
def update_followup(request, id):
    followup_id = int(id)
    try:
        fol_get = Followup.objects.get(id = followup_id)
    except Followup.DoesNotExist:
        return redirect('dashboard')
    form = FollowupForm(request.POST or None, instance = fol_get)
    if form.is_valid():
       form.save()
       return redirect('dashboard')
    return render(request, 'client/follow_up.html', {'upload_form':form})


@login_required(login_url='/')
def delete_Followup(request, id):
    fol_id = int(id)
    try:
        fol_data = Followup.objects.get(id = fol_id)
    except Followup.DoesNotExist:
        return redirect('dashboard')
    fol_data.status = '0'
    fol_data.save()
    return redirect('dashboard')



@login_required(login_url='/')
def info_client(request):
    return render(request, 'client/info_client.html')

@login_required(login_url='/')
def proj_dashboard(request):
    project = Project.objects.filter(status='1' , completed='0').order_by('-created')
    project_completed = Project.objects.filter(status='1', completed='1').order_by('-modified')
    proj_assign = Project_Assign.objects.filter(status='1', completed='0').order_by('-created')
    proj_assign_completed = Project_Assign.objects.filter(status='1', completed='1').order_by('-created')
    proj_inc = Project_income.objects.filter(status='1').order_by('-created')
    company_pro = Company_Profile.objects.filter(status='1').order_by('-created')
    expenses_pro = Extra_Expenses.objects.filter(status ='1').order_by('-created')
    tax_pro = Tax.objects.filter(status='1').order_by('-created') 

##pagination of project
    paginator = Paginator(project, 2)
    page_number = request.GET.get('page')
    proj_page = paginator.get_page(page_number)

##Paginator of Project Income
    paginator = Paginator(proj_inc, 2)
    page_number = request.GET.get('page')
    proj_inc_page = paginator.get_page(page_number)

##Complete Project
    paginator = Paginator(project_completed, 2)
    page_number = request.GET.get('page')
    proj_compplete_page = paginator.get_page(page_number)

## Pagination completed Assigned Project
    paginator = Paginator(proj_assign_completed, 2)
    page_number = request.GET.get('page')
    proj_assign_completed_page = paginator.get_page(page_number)

##PAgination for Assign Project
    paginator = Paginator(proj_assign, 2)
    page_number = request.GET.get('page')
    proj_assign_page = paginator.get_page(page_number)

## Pagination for company
    paginator = Paginator(company_pro, 2)
    page_number = request.GET.get('page')
    page_company = paginator.get_page(page_number)

## Pagination for Expenses
    paginator = Paginator(expenses_pro, 2)
    page_number = request.GET.get('page')
    page_expenses = paginator.get_page(page_number)

## Pagination for Tax
    paginator = Paginator(tax_pro, 2)
    page_number = request.GET.get('page')
    page_tax = paginator.get_page(page_number)



    context = {
               'proj_page':proj_page,
               'proj_compplete_page':proj_compplete_page,
               'proj_inc_page':proj_inc_page,
               'proj_assign_page':proj_assign_page,
               'proj_assign_completed_page':proj_assign_completed_page,
               'page_company':page_company,
               'page_expenses':page_expenses,
               'page_tax':page_tax,
            }
    return render(request, 'client/project_dashboard.html', context)


@login_required(login_url='/')
def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('proj_dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'proj_dashboard'}}">reload</a>""")
    else:      
        return render(request, 'client/create_project.html', {'upload_form':form})


@login_required(login_url='/')
def update_project(request, id):
    proj_id = int(id)
    try:
        proj_get = Project.objects.get(id = proj_id)
    except Project.DoesNotExist:
        return redirect('proj_dashboard')
    form = ProjectForm(request.POST or None, instance = proj_get)
    if form.is_valid():
       form.save()
       return redirect('proj_dashboard')
    return render(request, 'client/create_project.html', {'upload_form':form})


@login_required(login_url='/')
def delete_project(request, id):
    proj_id = int(id)
    try:
        proj_data = Project.objects.get(id = proj_id)
    except Project.DoesNotExist:
        return redirect('proj_dashboard')
    proj_data.status = '0'
    proj_data.save()
    return redirect('proj_dashboard')


@login_required(login_url='/')
def complete_project(request, id):
    proj_id = int(id)
    try:
        proj_data = Project.objects.get(id = proj_id)
    except Project.DoesNotExist:
        return redirect('proj_dashboard')
    proj_data.completed = 1
    proj_data.save()
    return redirect('proj_dashboard')

@login_required(login_url='/')
def uncomplete_project(request, id):
    proj_id = int(id)
    try:
        proj_data = Project.objects.get(id = proj_id)
    except Project.DoesNotExist:
        return redirect('proj_dashboard')
    proj_data.completed = 0
    proj_data.save()
    return redirect('proj_dashboard')


@login_required(login_url='/')
def project_income(request):
    form = Project_incomeForm()
    form1 = InvoiceForm()
    if request.method == 'POST':
        form = Project_incomeForm(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            obj = form.save()
            proj_name = obj.project_name
            print(proj_name)
            choice = form1.save(commit=False)
            proj = Project.objects.filter(project_name = proj_name)
            for ab in proj:
                client = ab.client_name
                project1_name = ab.project_name
                print(client)
            choice.client_name = client
            choice.project_name = project1_name
            choice.amount_received = obj.amount
            choice.date = obj.received_date
            choice.save()
            id = obj.project_name.id
            print(id)
            proj_amount = obj.amount
            ab = Project.objects.filter(id=id)
            for amt in ab:
                total_amt = amt.received_amount
                print(total_amt)
            to_update = Project.objects.filter(id=id).update(received_amount=total_amt + proj_amount )
            return redirect('proj_dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/proj_dashboard/'}}">reload</a>""")
    else:      
        return render(request, 'client/project_income.html', {'upload_form':form})


@login_required(login_url='/')
def update_project_income(request, id):
    proj_income_id = int(id)
    try:
        proj_income_get = Project_income.objects.get(id = proj_income_id)
    except Project_income.DoesNotExist:
        return redirect('proj_dashboard')
    form = Project_incomeForm(request.POST or None, instance = proj_income_get)
    if form.is_valid():
       form.save()
       return redirect('proj_dashboard')
    return render(request, 'client/project_income.html', {'upload_form':form})

@login_required(login_url='/')
def delete_project_income(request, id):
    proj_income_id = int(id)
    try:
        proj_income_data = Project_income.objects.get(id = proj_income_id)
    except Project_income.DoesNotExist:
        return redirect('proj_dashboard')
    proj_income_data.status = '0'
    proj_income_data.save()
    return redirect('proj_dashboard')

@login_required(login_url='/')
def assign_project(request):
    form = Project_AssignForm()
    if request.method == 'POST':
        form = Project_AssignForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            # id = obj.project_name.id
            # print(id)
            # proj_amount = obj.amount
            # ab = Project.objects.filter(id=id)
            # for amt in ab:
            #     total_amt = amt.amount
            #     print(total_amt)
            # to_update = Project.objects.filter(id=id).update(amount=total_amt + proj_amount)
            return redirect('proj_dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'proj_dashboard'}}">reload</a>""")
    else:      
        return render(request, 'client/assign_project.html', {'upload_form':form})


@login_required(login_url='/')
def update_assign_project(request, id):
    proj_income_id = int(id)
    try:
        proj_income_get = Project_Assign.objects.get(id = proj_income_id)
    except Project_Assign.DoesNotExist:
        return redirect('proj_dashboard')
    form = Project_AssignForm(request.POST or None, instance = proj_income_get)
    if form.is_valid():
       form.save()
       return redirect('proj_dashboard')
    return render(request, 'client/assign_project.html', {'upload_form':form})


@login_required(login_url='/')
def delete_project_assign(request, id):
    proj_assign_id = int(id)
    try:
        proj_assign_data = Project_Assign.objects.get(id = proj_assign_id)
    except Project_Assign.DoesNotExist:
        return redirect('proj_dashboard')
    proj_assign_data.status = '0'
    proj_assign_data.save()
    return redirect('proj_dashboard')

@login_required(login_url='/')
def complete_assign_project(request, id):
    proj_assign_id = int(id)
    try:
        proj_assign_data = Project_Assign.objects.get(id = proj_assign_id)
    except Project_Assign.DoesNotExist:
        return redirect('proj_dashboard')
    proj_assign_data.completed = 1
    proj_assign_data.save()
    return redirect('proj_dashboard')

@login_required(login_url='/')
def uncomplete_assign_project(request, id):
    proj_assign_id = int(id)
    try:
        proj_assign_data = Project_Assign.objects.get(id = proj_assign_id)
    except Project_Assign.DoesNotExist:
        return redirect('proj_dashboard')
    proj_assign_data.completed = 0
    proj_assign_data.save()
    return redirect('proj_dashboard')

@login_required(login_url='/')
def create_company(request):
    form = Company_ProfileForm()
    if request.method == 'POST':
        form = Company_ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect('proj_dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'proj_dashboard'}}">reload</a>""")
    else:      
        return render(request, 'client/create_company.html', {'upload_form':form})


@login_required(login_url='/')
def update_company(request, id):
    company_id = int(id)
    try:
        company_id_get = Company_Profile.objects.get(id = company_id)
    except Company_Profile.DoesNotExist:
        return redirect('proj_dashboard')
    form = Company_ProfileForm(request.POST or None, instance = company_id_get)
    if form.is_valid():
       form.save()
       return redirect('proj_dashboard')
    return render(request, 'client/create_company.html', {'upload_form':form})


@login_required(login_url='/')
def delete_company(request, id):
    company_id = int(id)
    try:
        company_data = Company_Profile.objects.get(id = company_id)
    except Company_Profile.DoesNotExist:
        return redirect('proj_dashboard')
    company_data.status = '0'
    company_data.save()
    return redirect('proj_dashboard')

@login_required(login_url='/')
def create_expenses(request):
    form = Extra_ExpensesForm()
    if request.method == 'POST':
        form = Extra_ExpensesForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect('proj_dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'proj_dashboard'}}">reload</a>""")
    else:      
        return render(request, 'client/expenses.html', {'upload_form':form})


@login_required(login_url='/')
def update_expenses(request, id):
    expenses_id = int(id)
    try:
        expenses_id_get = Extra_Expenses.objects.get(id = expenses_id)
    except Extra_Expenses.DoesNotExist:
        return redirect('proj_dashboard')
    form = Extra_ExpensesForm(request.POST or None, instance = expenses_id_get)
    if form.is_valid():
       form.save()
       return redirect('proj_dashboard')
    return render(request, 'client/expenses.html', {'upload_form':form})


@login_required(login_url='/')
def delete_expenses(request, id):
    expenses_id = int(id)
    try:
        expenses_data = expenses_Profile.objects.get(id = expenses_id)
    except expenses_Profile.DoesNotExist:
        return redirect('proj_dashboard')
    expenses_data.status = '0'
    expenses_data.save()
    return redirect('proj_dashboard')


@login_required(login_url='/')
def create_tax(request):
    form = TaxForm()
    if request.method == 'POST':
        form = TaxForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect('proj_dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'proj_dashboard'}}">reload</a>""")
    else:      
        return render(request, 'client/expenses.html', {'upload_form':form})


@login_required(login_url='/')
def update_tax(request, id):
    tax_id = int(id)
    try:
        tax_id_get = Tax.objects.get(id = tax_id)
    except Tax.DoesNotExist:
        return redirect('proj_dashboard')
    form = TaxForm(request.POST or None, instance = tax_id_get)
    if form.is_valid():
       form.save()
       return redirect('proj_dashboard')
    return render(request, 'client/expenses.html', {'upload_form':form})


@login_required(login_url='/')
def delete_tax(request, id):
    tax_id = int(id)
    try:
        tax_data = Tax.objects.get(id = tax_id)
    except Tax.DoesNotExist:
        return redirect('proj_dashboard')
    tax_data.status = '0'
    tax_data.save()
    return redirect('proj_dashboard')




def invoice(request, id):
    return render(request, 'client/invoice.html')


