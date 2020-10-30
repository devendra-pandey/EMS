from django.contrib import admin

# Register your models here.
from .models import Employee, HomeAddress, Certification, EmergencyContact, Beneficiary, Spouse, Deduction, \
    BankDetail, Allowance, StatutoryDeduction,Salary,Sallary_increament,Monthly_Salary

admin.site.site_header = "D2 EMS Admin"

admin.site.register(HomeAddress)
admin.site.register(Certification)
admin.site.register(EmergencyContact)
admin.site.register(Beneficiary)
admin.site.register(Spouse)
admin.site.register(Deduction)
admin.site.register(BankDetail)
admin.site.register(Allowance)
admin.site.register(StatutoryDeduction)
admin.site.register(Sallary_increament)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',
    # 'gender','start_date','marital_status','profile_image','status','created'
    )
    # search_fields = ('first_name','nationality')
    # date_hierarchy = ('created')
    # list_filter = ('created', 'marital_status')
    

@admin.register(Monthly_Salary)
class Monthly_SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee_name','leaves','total_working_days','total_salary')
    date_hierarchy = 'created'
    readonly_fields=('paid_leaves', )

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employe_name','emp_salary','incresed_sallary')
    readonly_fields = ('incresed_sallary',)
    
    def has_delete_permission(self, request, obj=None):
        return False


