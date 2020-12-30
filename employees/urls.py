from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('employee_admin', views.employee_admin , name='dashboard'),
    path('create/', views.employee_create, name='create_employee'),
    path('update_emp/<int:id>', views.update_employee, name='update_employee'),
    path('all_emp/', views.employees, name='employees'),
    path('view_emp/<int:id>', views.info, name='view_emp'),
    path('delete_emp/<int:id>', views.delete_emp, name='delete_emp'),
    path('all_sal/', views.all_sal),
    path('all_inc/', views.all_sal_increment),
    path('increase_Sal/',views.sallary_increment_create, name='increase_sal'),
    path('update_inc_sal/<int:id>', views.update_inc_sal, name='upadte_inc_sal'),
    path('delete_inc_sal/<int:id>', views.delete_inc_sal, name='delete_inc_sal'),
    path('all_monthly_sallary/', views.all_monthly_sallary, name='all_monthly_sallary'),
    path('month_Sal/', views.monthly_sal, name='month_sal'),
    path('update_month_Sal/<int:id>', views.update_monthly_sal, name='update_monthly_sal'),
    path('delete_monthly_sal/<int:id>', views.delete_monthly_sal, name='delete_monthly_sal'),
    
]