from django.db import models
from django.utils.html import format_html

# Create your models here.
TYPE_GENDER = (
        ('0', 'Female'),
        ('1', 'male'),
    )

TYPE_MARRIED = (
        ('0', 'Married'),
        ('1', 'Single'),
    )


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=11,choices=TYPE_GENDER)
    start_date = models.DateField()
    marital_status = models.CharField(max_length=10, choices=TYPE_MARRIED )
    dob = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=20, default="INDIA")
    mobile_number = models.CharField(max_length=13)
    residence_address = models.CharField(max_length=20)
    aadhar = models.CharField(max_length=20 , unique=True , null=True, blank=True)
    id_image = models.FileField(upload_to='static/Uploads/id/', null= True , blank=True)
    annual_allowance = models.IntegerField(default=21)
    balance_last_year = models.IntegerField(default=0)
    leave_status = models.CharField(max_length=45, default="At Work")
    profile_image = models.FileField(upload_to='static/Uploads/profile/', null= True , blank=True)
    End_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
      get_latest_by = 'created'



class Contacts(models.Model):
    contact_type = models.CharField(max_length=10, default="number")
    contact = models.CharField(max_length=15, null=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class HomeAddress(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    district = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    sub_county = models.CharField(max_length=20)
    village = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.district


class Certification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year_completed = models.CharField(max_length=4)
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class EmergencyContact(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    relationship = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Beneficiary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    relationship = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=40)
    percentage = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Spouse(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    national_id = models.CharField(max_length=40)
    dob = models.DateField()
    occupation = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name


class Deduction(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_advance = models.IntegerField(default=0)
    police_fine = models.IntegerField(default=0)

    def __str__(self):
        return self.employee.first_name + " Deduction"


class StatutoryDeduction(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    local_service_tax = models.FloatField()

    def __str__(self):
        return f"Local service tax {self.local_service_tax}"


class Leave(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20)
    department = models.CharField(max_length=15)
    apply_date = models.DateField()
    _year = models.CharField(max_length=4)
    start_date = models.DateField()
    end_date = models.DateField()
    supervisor = models.CharField(max_length=45)
    sup_Status = models.CharField(max_length=15)
    hod = models.CharField(max_length=45)
    hod_status = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class BankDetail(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name_of_bank = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    bank_account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name_of_bank, self.bank_account_number, self.ifsc_code)


class Allowance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)


class Supervision(models.Model):
    supervisor = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="supervisees")
    supervisee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="supervisors")

class Monthly_Salary(models.Model):
    employee_name = models.ForeignKey('Employee', on_delete=models.CASCADE)
    leaves = models.IntegerField()
    paid_leaves = models.IntegerField(default=1)
    total_working_days = models.IntegerField(default=1)
    total_salary = models.CharField(max_length=20, default='0')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def calculate_salary(self):
        emp_name = Salary.objects.get(employee_name = self.employee_name)
        print("hey hii")
        print(emp_name)
        total_days = self.total_working_days - self.leaves + self.paid_leaves
        print(total_days)
        base_salary_emp = emp_name.emp_salary / self.total_working_days
        print(base_salary_emp)
        salary_1 = total_days * base_salary_emp
        self.total_salary = salary_1
        return self.total_salary
        

    def save(self,*args,**kwargs):
        self.total_salary = str(self.calculate_salary())
        super().save(*args, **kwargs)

class Salary(models.Model):
    employe_name = models.ForeignKey('Employee', on_delete=models.CASCADE)
    emp_salary = models.IntegerField(default= 10000)
    incresed_sallary = models.IntegerField(null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Sallary_increament(models.Model):
    employe_name = models.ForeignKey('Employee', on_delete=models.CASCADE)
    hike_sallary = models.IntegerField()
    description = models.CharField(max_length=300)
    Increment_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    
    
