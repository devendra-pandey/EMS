from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect
from client.models import Client, Project



class ProjectForm(forms.Form):
    class Meta:
           model = Project
           fields = ['__all__']
           widgets = {
               'status': forms.RadioSelect()
           }   