from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('timeline/', views.timeline, name='timeline'),
    path('data_projects/', views.data_projects, name='data_projects'),
    path('view_proj/<int:id>', views.proj_info),
    path('project_income_detail/', views.proj_income_details, name='proj_inc_detail'),
    path('proj_assign_details/', views.proj_assign_details, name='proj_assign_details')
    
    
    
    ]