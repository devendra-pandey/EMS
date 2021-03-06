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


@login_required(login_url='/')
def client_create(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'client'}}">reload</a>""")
    else:  
        return render(request, 'client/client_create.html', {'upload_form':form})

@login_required(login_url='/')
def update_client(request, id):
    client_id = int(id)
    try:
        client_get = Client.objects.get(id = client_id)
    except Client.DoesNotExist:
        return redirect('client')
    form = ClientForm(request.POST or None, instance = client_get)
    if form.is_valid():
       form.save()
       return redirect('client')
    return render(request, 'client/client_create.html', {'upload_form':form})

@login_required(login_url='/')
def delete_client(request, id):
    client_id = int(id)
    try:
        client_data = Client.objects.get(id = client_id)
    except Client.DoesNotExist:
        return redirect('client')
    client_data.status = '0'
    client_data.save()
    return redirect('client')


@login_required(login_url='/')
def create_enquiry(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully saved')
            return redirect('all_enq')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'all_enq'}}">reload</a>""")
    else:      
        return render(request, 'client/enquiry.html', {'upload_form':form})

@login_required(login_url='/')
def update_enquiry(request, id):
    enquiry_id = int(id)
    try:
        enq_get = Enquiry.objects.get(id = enquiry_id)
    except Enquiry.DoesNotExist:
        return redirect('all_enq')
    form = EnquiryForm(request.POST or None, instance = enq_get)
    if form.is_valid():
       form.save()
       return redirect('all_enq')
    return render(request, 'client/enquiry.html', {'upload_form':form})

@login_required(login_url='/')
def delete_enquiry(request, id):
    enq_id = int(id)
    try:
        enq_data = Enquiry.objects.get(id = enq_id)
    except Enquiry.DoesNotExist:
        return redirect('all_enq')
    enq_data.status = '0'
    enq_data.save()
    return redirect('all_enq')


@login_required(login_url='/')
def create_followup(request):
    form = FollowupForm()
    if request.method == 'POST':
        form = FollowupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_followup')
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
        return redirect('all_followup')
    form = FollowupForm(request.POST or None, instance = fol_get)
    if form.is_valid():
       form.save()
       return redirect('all_followup')
    return render(request, 'client/follow_up.html', {'upload_form':form})


@login_required(login_url='/')
def delete_Followup(request, id):
    fol_id = int(id)
    try:
        fol_data = Followup.objects.get(id = fol_id)
    except Followup.DoesNotExist:
        return redirect('all_followup')
    fol_data.status = '0'
    fol_data.save()
    return redirect('all_followup')


@login_required(login_url='/')
def client(request):
    client = Client.objects.all().filter(status = '1').order_by('-created')
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
                'client_all':client_all,
            }
    return render(request, 'client/clients.html',context)

@login_required(login_url='/')
def info_client(request, id):
    client_info = get_object_or_404(Client, id=id)
    context = {
        'client_info':client_info
    }
    return render(request, 'client/info_client.html', context)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@login_required(login_url='/')
def all_enquiry(request):
    enq = Enquiry.objects.all().filter(status = '1').order_by('-created')

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
    }


    return render(request, 'client/all_enquiry.html', context)

@login_required(login_url='/')
def all_followup(request):
    feedback = Followup.objects.filter(status='1').order_by('-created')

##FeedBack Pagination
    paginator = Paginator(feedback, 2)
    page_number = request.GET.get('page')
    feedback_obj = paginator.get_page(page_number)

    context = {
        'feedback_obj':feedback_obj,

    }
    return render(request, 'client/all_followup.html', context)



@login_required(login_url='/')
def alert(request):
    enq = Enquiry.objects.all().filter(status = '1').order_by('-created')
    feedback = Followup.objects.filter(status='1').order_by('-created')


    context = {
        'enq':enq,
        'feedback':feedback,
        'datetime':datetime,

    }
    return render(request, 'client/alert.html', context)

@login_required(login_url='/')
def create_project(request):
    form = ProjectForm()
    form1 = InvoiceForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('data_projects')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'data_projects'}}">reload</a>""")
    else:      
        return render(request, 'client/create_project.html', {'upload_form':form})


@login_required(login_url='/')
def update_project(request, id):
    proj_id = int(id)
    try:
        proj_get = Project.objects.get(id = proj_id)
    except Project.DoesNotExist:
        return redirect('data_projects')
    form = ProjectForm(request.POST or None, instance = proj_get)
    if form.is_valid():
       form.save()
       return redirect('data_projects')
    return render(request, 'client/create_project.html', {'upload_form':form})


@login_required(login_url='/')
def delete_project(request, id):
    proj_id = int(id)
    try:
        proj_data = Project.objects.get(id = proj_id)
    except Project.DoesNotExist:
        return redirect('data_projects')
    proj_data.status = '0'
    proj_data.save()
    return redirect('data_projects')


@login_required(login_url='/')
def complete_project(request, id):
    proj_id = int(id)
    try:
        proj_data = Project.objects.get(id = proj_id)
    except Project.DoesNotExist:
        return redirect('data_projects')
    proj_data.completed = 1
    proj_data.save()
    return redirect('data_projects')

@login_required(login_url='/')
def uncomplete_project(request, id):
    proj_id = int(id)
    try:
        proj_data = Project.objects.get(id = proj_id)
    except Project.DoesNotExist:
        return redirect('data_projects')
    proj_data.completed = 0
    proj_data.save()
    return redirect('data_projects')


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
            return redirect('data_projects')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/data_projects/'}}">reload</a>""")
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
        return redirect('data_projects')
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
       return redirect('data_projects')
    return render(request, 'client/project_income.html', {'upload_form':form})

@login_required(login_url='/')
def delete_project_income(request, id):
    proj_income_id = int(id)
    try:
        proj_income_data = Project_income.objects.get(id = proj_income_id)
    except Project_income.DoesNotExist:
        return redirect('data_projects')
    
    id = proj_income_data.project_name.id
    ab = Project.objects.filter(id=id)
    for amt in ab:
        total_amt = amt.received_amount
        print(total_amt)
    proj_income_data.status = '0'
    proj_income_data.save()
    to_update = Project.objects.filter(id=id).update(received_amount=total_amt - proj_income_data.amount )
    return redirect('data_projects')

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
            return redirect('data_projects')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'data_projects'}}">reload</a>""")
    else:      
        return render(request, 'client/assign_project.html', {'upload_form':form})


@login_required(login_url='/')
def update_assign_project(request, id):
    proj_income_id = int(id)
    try:
        proj_income_get = Project_Assign.objects.get(id = proj_income_id)
    except Project_Assign.DoesNotExist:
        return redirect('data_projects')
    form = Project_AssignForm(request.POST or None, instance = proj_income_get)
    if form.is_valid():
       form.save()
       return redirect('data_projects')
    return render(request, 'client/assign_project.html', {'upload_form':form})


@login_required(login_url='/')
def delete_project_assign(request, id):
    proj_assign_id = int(id)
    try:
        proj_assign_data = Project_Assign.objects.get(id = proj_assign_id)
    except Project_Assign.DoesNotExist:
        return redirect('data_projects')
    proj_assign_data.status = '0'
    proj_assign_data.save()
    return redirect('data_projects')

@login_required(login_url='/')
def complete_assign_project(request, id):
    proj_assign_id = int(id)
    try:
        proj_assign_data = Project_Assign.objects.get(id = proj_assign_id)
    except Project_Assign.DoesNotExist:
        return redirect('data_projects')
    proj_assign_data.completed = 1
    proj_assign_data.save()
    return redirect('data_projects')

@login_required(login_url='/')
def uncomplete_assign_project(request, id):
    proj_assign_id = int(id)
    try:
        proj_assign_data = Project_Assign.objects.get(id = proj_assign_id)
    except Project_Assign.DoesNotExist:
        return redirect('data_projects')
    proj_assign_data.completed = 0
    proj_assign_data.save()
    return redirect('data_projects')

@login_required(login_url='/')
def create_company(request):
    form = Company_ProfileForm()
    if request.method == 'POST':
        form = Company_ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect('data_projects')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'data_projects'}}">reload</a>""")
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
