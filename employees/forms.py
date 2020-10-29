from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect
from employees.models import Employee,Monthly_Salary
from django.forms import ClearableFileInput, ModelForm



class EmployeeForm(forms.ModelForm):
    class Meta:
           model = Employee
           fields = [
               'first_name',
               'last_name',
               'gender',
               'start_date',
               'marital_status',
               'dob',
               'mobile_number',
               'residence_address',
               'aadhar',
               'id_image',
               'profile_image'

           ]
           widgets = {
               'gender': forms.RadioSelect(),
               'id_image': ClearableFileInput(attrs={'multiple': True}),
               'marital_status': forms.RadioSelect()
           }   

