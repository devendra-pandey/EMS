from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect
from .models import Client, Project ,Enquiry , Followup , Project_income , Project_Assign , Company_Profile, Tax, Extra_Expenses , Invoice


class DateInput(forms.DateInput):
    input_type = 'date'

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['status']


class Company_ProfileForm(forms.ModelForm):
    class Meta:
        model = Company_Profile
        fields = '__all__'
        exclude = ['status']

class Extra_ExpensesForm(forms.ModelForm):
    class Meta:
        model = Extra_Expenses
        fields = '__all__'
        exclude = ['status']
        widgets = {
            'date' : DateInput
        }

class TaxForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = '__all__'
        exclude = ['status']

class Project_AssignForm(forms.ModelForm):
    class Meta:
        model = Project_Assign
        fields = '__all__'
        exclude = ['status', 'completed']
        widgets = {
            'start_date' : DateInput,
            'end_date' : DateInput,
            'actual_end_date' : DateInput,
        }

class Project_incomeForm(forms.ModelForm):
    class Meta:
        model = Project_income
        fields = '__all__'
        exclude = ['status']
        widgets = {
            'received_date':DateInput,
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['status','completed','received_amount','total_amount']
        widgets = {
               'end_date': DateInput,               
           }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['status']

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'
        exclude = ['status']
        widgets = {
               'enquiry_date': DateInput,               
           }

class FollowupForm(forms.ModelForm):
    class Meta:
        model= Followup
        fields = '__all__'