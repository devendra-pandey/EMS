from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect
from employees.models import Employee,Monthly_Salary
from django.forms import ClearableFileInput



class EmployeeForm(forms.Form):
    class Meta:
           model = Employee
           fields = ['__all__']
           widgets = {
               'gender': forms.RadioSelect(),
               'id_image': ClearableFileInput(attrs={'multiple': True}),
               'marital_status': forms.RadioSelect()
           }   

