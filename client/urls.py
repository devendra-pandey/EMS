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
    path('client/<int:id>', views.info_client, name='info_client'),
]