from django.contrib import admin

# Register your models here.

from .models import Project,Client,Contacts,Enquiry


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company_name','first_name','last_name','nationality','linkedln_profile','whatsapp_number','mobile_no',)
    list_display_links = ('linkedln_profile',)
    ordering = ('company_name',)
    search_fields = ('company_name,first_name','nationality')


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('client_name','enquiry_date','proposal_file','comment','created',)
    ordering = ('created',)


admin.site.register(Contacts)
admin.site.register(Project)
