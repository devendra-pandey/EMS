from django.db import models
from employees.models import Employee
import datetime
from django.utils.html import format_html
# Create your models here.


TYPE_STATUS = (
        ('0', 'Deactive'),
        ('1', 'Active'),
    )




class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30 ,null=True ,blank=True)
    linkedln_profile = models.CharField(max_length=70 ,null=True ,blank=True)
    whatsapp_number = models.IntegerField(null=True ,blank=True)
    nationality = models.CharField(max_length=20 , null=True ,blank=True)
    mobile_no = models.CharField(max_length=20, null=True ,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def linkedln_taf(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.linkedln_profile.url))

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Contacts(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=10, default="number")
    contact = models.CharField(max_length=15, null=False)
    

class Project(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50)
    project_type = models.CharField(max_length=50)
    project_files = models.FileField(upload_to='static/Uploads/projects/', null=True)
    amount = models.IntegerField(default=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Enquiry(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    enquiry_date = models.DateField()
    proposal_file = models.FileField(upload_to='static/Uploads/proposals/', null= True)
    comment = models.CharField(max_length=1000, null = True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def older_than_ten_days(self):
        return (datetime.date.today() - self.enquiry_date).days > 10
