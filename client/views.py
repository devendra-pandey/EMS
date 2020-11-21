from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ClientForm , EnquiryForm ,FollowupForm , ProjectForm , Project_incomeForm, Project_AssignForm , Company_ProfileForm , Extra_ExpensesForm , TaxForm , InvoiceForm
from .models import Enquiry ,Followup , Project, Project_income , Project_Assign , Client , Company_Profile , Extra_Expenses , Tax , Invoice
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
import datetime
from django.template.defaulttags import register
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.contrib import messages

# register = template.library()

# @register.filter()
# def addDays(days):
#    newDate = datetime.date.today() + datetime.timedelta(days=days)
#    return newDate

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
def enquiry_admin(request):
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
                'enq':enq,
                'feedback':feedback,
                'datetime':datetime,
                
            }
    return render(request, 'employees/enquiry_dashboard.html',context)



@login_required(login_url='/')
def create_enquiry(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully saved')
            return redirect('enquiry_admin')
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
        return redirect('enquiry_admin')
    form = EnquiryForm(request.POST or None, instance = enq_get)
    if form.is_valid():
       form.save()
       return redirect('enquiry_admin')
    return render(request, 'client/enquiry.html', {'upload_form':form})

@login_required(login_url='/')
def delete_enquiry(request, id):
    enq_id = int(id)
    try:
        enq_data = Enquiry.objects.get(id = enq_id)
    except Enquiry.DoesNotExist:
        return redirect('enquiry_admin')
    enq_data.status = '0'
    enq_data.save()
    return redirect('enquiry_admin')


@login_required(login_url='/')
def create_followup(request):
    form = FollowupForm()
    if request.method == 'POST':
        form = FollowupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('enquiry_admin')
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
        return redirect('enquiry_admin')
    form = FollowupForm(request.POST or None, instance = fol_get)
    if form.is_valid():
       form.save()
       return redirect('enquiry_admin')
    return render(request, 'client/follow_up.html', {'upload_form':form})


@login_required(login_url='/')
def delete_Followup(request, id):
    fol_id = int(id)
    try:
        fol_data = Followup.objects.get(id = fol_id)
    except Followup.DoesNotExist:
        return redirect('enquiry_admin')
    fol_data.status = '0'
    fol_data.save()
    return redirect('enquiry_admin')



@login_required(login_url='/')
def info_client(request):
    return render(request, 'client/info_client.html')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


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
    tot_proj = Project.objects.all().count()
    comp_proj = Project.objects.filter(status='1', completed='1').count()
    going_proj = Project.objects.filter(status='1', completed='0').count()
    
    years = Extra_Expenses.objects.dates('date','year')
    expenses = Extra_Expenses.objects.all().filter(status='1').values()
    amounts = {}

    for expense in expenses:
        year = expense['date'].year
        if year in amounts:
            amounts[year] = amounts[year] + expense['expense_amount']
        else:
            amounts[year] = expense['expense_amount']

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
               'years': years, 
               'amounts': amounts,
               'months': months, 
               'amount': amount,
               'proj_page':proj_page,
               'proj_compplete_page':proj_compplete_page,
               'proj_inc_page':proj_inc_page,
               'proj_assign_page':proj_assign_page,
               'proj_assign_completed_page':proj_assign_completed_page,
               'page_company':page_company,
               'page_expenses':page_expenses,
               'page_tax':page_tax,
               'tot_proj':tot_proj,
               'comp_proj':comp_proj,
               'going_proj':going_proj,
            }
    return render(request, 'client/project_dashboard.html', context)


@login_required(login_url='/')
def create_project(request):
    form = ProjectForm()
    form1 = InvoiceForm()
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
        if form.is_valid():
            obj = form.save()
            proj_id = obj.id
            proj_name = obj.project_name
            proj_client_name = obj.project_name.client_name
            proj_company_rec = obj.company_received_name
            proj_date = obj.received_date
            proj_amount = obj.amount
            proj_payment_type = obj.payment_method
            print("******")
            print(proj_id)
            total_t = proj_amount * 18/100
            total_dis = proj_amount * 10/100
            proj_tot_amt = total_t + proj_amount - total_dis
            print("*****^^^^***")
            print(proj_tot_amt)
            choice = form1.save(commit=False)
            choice.client_name = proj_client_name
            choice.project_name = proj_name
            choice.by_company_name = proj_company_rec
            choice.amount_received = proj_amount
            choice.date = proj_date
            choice.payment_method = proj_payment_type
            choice.project_income_id = proj_id
            choice.tax = total_t
            choice.discount = total_dis
            choice.total_amount = proj_tot_amt
            choice.save()
            id = obj.project_name.id
            print(id)
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
        ab1 = proj_income_get.amount
        print(ab1)
    except Project_income.DoesNotExist:
        return redirect('proj_dashboard')
    form = Project_incomeForm(request.POST or None, instance = proj_income_get)
    if form.is_valid():
       obj = form.save()
       proj_amount = obj.amount
       id = obj.project_name.id
       print(id)
       ab = Project.objects.filter(id=id)
       for amt in ab:
           total_amt = amt.received_amount
           print(total_amt)
       to_update = Project.objects.filter(id=id).update(received_amount=total_amt + proj_amount - ab1 )
       return redirect('proj_dashboard')
    return render(request, 'client/project_income.html', {'upload_form':form})

@login_required(login_url='/')
def delete_project_income(request, id):
    proj_income_id = int(id)
    try:
        proj_income_data = Project_income.objects.get(id = proj_income_id)
    except Project_income.DoesNotExist:
        return redirect('proj_dashboard')
    
    id = proj_income_data.project_name.id
    ab = Project.objects.filter(id=id)
    for amt in ab:
        total_amt = amt.received_amount
        print(total_amt)
    proj_income_data.status = '0'
    proj_income_data.save()
    to_update = Project.objects.filter(id=id).update(received_amount=total_amt - proj_income_data.amount )
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
        expenses_data = Extra_Expenses.objects.get(id = expenses_id)
    except Extra_Expenses.DoesNotExist:
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


@login_required(login_url='/')
def invoice(request, id):
    invoice_info = get_object_or_404(Invoice, project_income_id=id)
    print("**++**")
    print(invoice_info)

    context = {
        'invoice_info':invoice_info,
    }
    return render(request, 'client/invoice.html', context)




# @login_required(login_url='/')
# def html_to_pdf_view(request, id):
#     invoice_info = get_object_or_404(Invoice, project_income_id=id)
#     print("**++**")
#     print(invoice_info)

#     context = {
#         'invoice_info':invoice_info,
#     }
#     html_string = render_to_string('client/invoice.html', context)

#     html = HTML(string=html_string)
#     html.write_pdf(target='/tmp/mypdf.pdf');

#     fs = FileSystemStorage('/tmp')
#     with fs.open('mypdf.pdf') as pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
#         return response

#     return response
