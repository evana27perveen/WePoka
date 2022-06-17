from django.urls import path
from . import views

app_name = 'App_post'

urlpatterns = [
    path('', views.home, name='home'),
    path('partner-request/', views.partner_request, name='partner-request'),
    path('job-post/', views.job_post, name='job-post'),
    path('display-requests/', views.display_partner_requests, name='display-requests'),
    path('apply/<int:pk>/', views.apply_for_participation, name='apply-for-participation')
]
