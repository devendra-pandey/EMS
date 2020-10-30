from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect
from .models import Client, Project ,Enquiry , Followup


class DateInput(forms.DateInput):
    input_type = 'date'


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