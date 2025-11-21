from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='job_list'),
    path('new/', views.JobCreateView.as_view(), name='job_create'),
    path('<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    
    # THIS IS THE LINE YOU ARE MISSING OR HAVE A TYPO IN:
    path('<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
    
    # This is the line for the edit feature we just added:
    path('<int:pk>/edit/', views.JobUpdateView.as_view(), name='job_edit'),
]