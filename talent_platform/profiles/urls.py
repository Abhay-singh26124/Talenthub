from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update_profile, name='profile_update'),
    path('<int:pk>/', views.CandidateProfileDetailView.as_view(), name='profile_detail'),
]