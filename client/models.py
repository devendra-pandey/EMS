from django.db import models
from employees.models import Employee
import datetime
from django.utils.html import format_html
# Create your models here.
TYPE_PROJECT = (
        ('Android', 'Android'),
        ('Ecommerce', 'Ecommerce'),
        ('ERP', 'ERP'),
        ('CMS', 'CMS'),
        ('Webapp','webapp'),
        ('Desktop_App','Desktop_App')
    )

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30 ,null=True ,blank=True)
    linkedln_profile = models.CharField(max_length=500 ,null=True ,blank=True)
    whatsapp_number = models.CharField(max_length=12, null=True ,blank=True)
    nationality = models.CharField(max_length=20 , null=True ,blank=True)
    mobile_no = models.CharField(max_length=20, null=True ,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default="1")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
      get_latest_by = 'created'
    
class Project(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100 , unique=True)
    project_type = models.CharField(max_length=50, choices=TYPE_PROJECT)
    project_files = models.FileField(upload_to='static/Uploads/projects/', null=True)
    advance_amount = models.IntegerField(default=0, blank=True, null=True)
    received_amount = models.IntegerField(default=0, blank=True, null=True)
    total_amount = models.IntegerField(default=0, blank=True , null=True)
    end_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default='0')
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

    def calculate_amt(self):
        total_amt = self.advance_amount
        self.received_amount = total_amt 
        return self.received_amount 

    def save(self,*args,**kwargs):
        self.received_amount = str(self.calculate_amt())
        super().save(*args, **kwargs)

class Project_income(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    received_date = models.DateField()
    comment = models.CharField(max_length=1000, null = True,blank=True)
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Enquiry(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    enquiry_date = models.DateField()
    proposal_file = models.FileField(upload_to='static/Uploads/proposals/', null= True)
    comment = models.CharField(max_length=1000, null = True,blank=True)
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

class Followup(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    Comment = models.CharField(max_length=10000, null=True, blank=True)
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Project_Assign(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    employe_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    actual_end_date = models.DateField()
    completed = models.BooleanField(default='0')
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.pk

class Invoice(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, blank=True, null=True) 
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Tax(models.Model):
    Tax_name = models.CharField(max_length=10)
    Tax_value = models.IntegerField()