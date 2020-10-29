from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect
from .models import Client, Project ,Enquiry


class DateInput(forms.DateInput):
    input_type = 'date'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'
        widgets = {
               'enquiry_date': DateInput,               
           }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
