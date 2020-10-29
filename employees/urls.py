from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('employee_admin', views.employee_admin , name='dashboard'),
    path('create/', views.employee_create, name='create_employee'),
    path('update_emp/<int:id>', views.update_employee, name='update_employee'),
    path('view_emp/<int:id>', views.info, name='view_emp'),
    path('Add_sallary/', views.sallary, name='sallary' ),

]