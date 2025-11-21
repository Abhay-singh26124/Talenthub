from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CandidateProfile
from .forms import CandidateProfileForm
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin  # <-- THIS WAS THE MISSING LINE
from jobs.views import RecruiterRequiredMixin # Make sure this is imported

@login_required
def update_profile(request):
    # Only Candidates can update profiles
    if request.user.role != 'CANDIDATE':
        return redirect('job_list') 
    
    profile, created = CandidateProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = CandidateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CandidateProfileForm(instance=profile)
        
    return render(request, 'profiles/profile_form.html', {'form': form})

# This class needs the imports above to work
class CandidateProfileDetailView(LoginRequiredMixin, RecruiterRequiredMixin, DetailView):
    model = CandidateProfile
    template_name = 'profiles/profile_detail.html' 
    context_object_name = 'profile'