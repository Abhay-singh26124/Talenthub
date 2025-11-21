from django.shortcuts import render, redirect, get_object_or_404 # <-- THIS LINE IS FIXED
from django.contrib.auth.decorators import login_required
from jobs.models import JobListing
from .models import Application
from profiles.models import CandidateProfile
from django.http import HttpResponseForbidden

@login_required
def apply_for_job(request, job_id):
    if request.user.role != 'CANDIDATE':
        return redirect('job_list')
    job = get_object_or_404(JobListing, id=job_id) # Using get_object_or_404 here too is good practice
    has_applied = Application.objects.filter(job=job, candidate=request.user).exists()
    if not has_applied:
        profile, created = CandidateProfile.objects.get_or_create(user=request.user)
        Application.objects.create(job=job, candidate=request.user)
    return redirect('dashboard')

@login_required
def dashboard(request):
    context = {}
    
    if request.user.role == 'CANDIDATE':
        applications = Application.objects.filter(candidate=request.user).order_by('-applied_at')
        context['applications'] = applications
        
    elif request.user.role == 'RECRUITER':
        jobs_posted = JobListing.objects.filter(posted_by=request.user).order_by('-created_at')
        context['jobs_posted'] = jobs_posted
        context['status_choices'] = Application.STATUS_CHOICES

    return render(request, 'applications/dashboard.html', context)

@login_required
def update_application_status(request, app_id):
    if request.method == 'POST':
        app = get_object_or_404(Application, id=app_id)
        
        # Security check: Is the logged-in user the owner of the job?
        if request.user != app.job.posted_by:
            return HttpResponseForbidden("You are not authorized to change this application.")
            
        new_status = request.POST.get('status')
        if new_status in [choice[0] for choice in Application.STATUS_CHOICES]:
            app.status = new_status
            app.save()
            
        return redirect('dashboard')
    
    return redirect('dashboard')