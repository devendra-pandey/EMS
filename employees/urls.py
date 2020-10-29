from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('employee_admin', views.employee_admin , name='dashboard'),
    path('create/', views.employee_create, name='create_employee'),
    path('info/<int:id>', views.info, name='info_emp_client'),
]