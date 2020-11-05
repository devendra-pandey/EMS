from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('create_client/', views.client_create, name='create_client'),
    path('update_client/<int:id>', views.update_client, name='update_client'),
    path('delete_client/<int:id>', views.delete_client, name='delete_client'),
    path('add_enquiry/', views.create_enquiry, name='create_enquiry'),
    path('update_enquiry/<int:id>', views.update_enquiry, name='update_enquiry'),
    path('delete_enquiry/<int:id>', views.delete_enquiry, name='delete_enquiry'),
    path('follow_up_create/', views.create_followup, name='create_followup'),
    path('update_followup/<int:id>', views.update_followup, name='update_followup'),
    path('delete_followup/<int:id>', views.delete_Followup, name='delete_followup'),
    path('client/<int:id>', views.info_client, name='info_client'),
    path('proj_dashboard/', views.proj_dashboard, name='proj_dashboard'),
    path('create_project/', views.create_project, name='create_project'),
    path('update_project/<int:id>', views.update_project, name='update_project'),
    path('delete_project/<int:id>', views.delete_project, name='delete_project'),
    path('complete_project/<int:id>', views.complete_project, name='complete_project'),
    path('uncomplete_project/<int:id>', views.uncomplete_project, name='uncomplete_project'),
    path('add_project_income/', views.project_income, name='project_income'),
    path('update_project_income/<int:id>', views.update_project_income, name='update_project_income'),
    path('delete_project_income/<int:id>', views.delete_project_income, name='delete_project_income'),
    path('assign_project/', views.assign_project, name='assign_project'),
    path('update_assign_project/<int:id>', views.update_assign_project, name='update_assign_project'),
    path('delete_project_assign/<int:id>', views.delete_project_assign, name='delete_project_assign'),
    path('complete_assign_project/<int:id>', views.complete_assign_project, name='complete_project'),
    path('uncomplete_assign_project/<int:id>', views.uncomplete_assign_project, name='uncomplete_assign_project'),
    path('create_company/', views.create_company, name='create_company'),
    path('update_company/<int:id>', views.update_company, name='update_company'),
    path('delete_company/<int:id>', views.delete_company, name='delete_company'),
    path('create_expenses/', views.create_expenses, name='create_expenses'),
    path('update_expenses/<int:id>', views.update_expenses, name='update_expenses'),
    path('delete_expenses/<int:id>', views.delete_expenses, name='delete_expenses'),
    path('create_tax/', views.create_tax, name='create_tax'),
    path('update_tax/<int:id>', views.update_tax, name='update_tax'),
    path('delete_tax/<int:id>', views.delete_tax, name='delete_tax'),
    path('invoice/<int:id>', views.invoice, name='invoice'),

]