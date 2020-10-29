from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect
from employees.models import Employee,Monthly_Salary,Salary
from django.forms import ClearableFileInput, ModelForm



class DateInput(forms.DateInput):
    input_type = 'date'


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
               'start_date': DateInput,
               'dob':DateInput,
               
           }   


class SallaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = [
               'employee_name',
               'emp_salary',
           ]