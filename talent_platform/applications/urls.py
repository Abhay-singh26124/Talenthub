from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), # The homepage will be the dashboard
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('application/update/<int:app_id>/', views.update_application_status, name='update_application_status'),
]