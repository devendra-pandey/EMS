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

TYPE_PAYMENT = (
        ('Cash', 'Cash'),
        ('Bank Transfer', 'Bank Transfer'),
        
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
    project_files = models.FileField(upload_to='static/Uploads/projects/', null=True , blank=True)
    advance_amount = models.IntegerField(default=0)
    received_amount = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)
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

class Tax(models.Model):
    tax_name = models.CharField(max_length=10)
    tax_value = models.IntegerField()
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Extra_Expenses(models.Model):
    Employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    client_name = models.ForeignKey(Client , on_delete=models.CASCADE, null=True , blank=True )
    other = models.CharField(max_length=100, null=True, blank=True)
    expense_amount = models.IntegerField(default=0)
    date = models.DateField()
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Company_Profile(models.Model):
    company_name = models.CharField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    Address  = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

class Project_income(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    company_received_name = models.ForeignKey(Company_Profile, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    received_date = models.DateField()
    payment_method = models.CharField(max_length=50, choices=TYPE_PAYMENT)
    comment = models.CharField(max_length=1000, null = True,blank=True)
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.pk

class Invoice(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    by_company_name = models.ForeignKey(Company_Profile, on_delete=models.CASCADE)
    project_income_id = models.IntegerField(unique=True)
    payment_method = models.CharField(max_length=50)
    amount_received = models.IntegerField(default='0')
    tax = models.IntegerField(default='18')
    discount = models.FloatField(default='10.0')
    total_amount = models.IntegerField(default='0')
    date = models.DateField()
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
