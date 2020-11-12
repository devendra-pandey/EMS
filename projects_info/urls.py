from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('timeline/', views.timeline, name='timeline'),
    path('employee_data/', views.employee_data, name='employee_data'),
    path('data_projects/', views.data_projects, name='data_projects'),
    
    
    
    ]