from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from client.models import Client
from django.contrib.auth.decorators import login_required
from .forms import ClientForm , EnquiryForm ,FollowupForm
from .models import Enquiry ,Followup

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