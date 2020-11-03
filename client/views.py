from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from client.models import Client
from django.contrib.auth.decorators import login_required
from .forms import ClientForm , EnquiryForm ,FollowupForm , ProjectForm , Project_incomeForm
from .models import Enquiry ,Followup , Project, Project_income

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


def proj_dashboard(request):
    project = Project.objects.filter(status='1' , completed='0').order_by('-created')
    project_completed = Project.objects.filter(status='1', completed='1').order_by('-modified')
    proj_inc = Project_income.objects.all()

    context = {
               'project': project,
               'project_completed':project_completed,
               'proj_inc':proj_inc,
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
    if request.method == 'POST':
        form = Project_incomeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            id = obj.project_name.id
            print(id)
            proj_amount = obj.amount
            ab = Project.objects.filter(id=id)
            for amt in ab:
                total_amt = amt.amount
                print(total_amt)
            to_update = Project.objects.filter(id=id).update(amount=total_amt + proj_amount)
            return redirect('proj_dashboard')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'proj_dashboard'}}">reload</a>""")
    else:      
        return render(request, 'client/project_income.html', {'upload_form':form})



@login_required(login_url='/')
def update_project(request, id):
    proj_income_id = int(id)
    try:
        proj_income_get = Project_income.objects.get(id = proj_income_id)
    except Project_income.DoesNotExist:
        return redirect('proj_dashboard')
    form = Project_incomeForm(request.POST or None, instance = proj_get)
    if form.is_valid():
       form.save()
       return redirect('proj_dashboard')
    return render(request, 'client/create_project.html', {'upload_form':form})
