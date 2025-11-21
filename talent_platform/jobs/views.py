# 1. Make sure UpdateView is imported
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import JobListing
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from applications.models import Application
from django.urls import reverse_lazy

# This mixin checks if the user is a recruiter
class RecruiterRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'RECRUITER'

# This mixin checks if the logged-in user is the one who posted the job
class JobOwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        job = self.get_object()
        return self.request.user == job.posted_by

class JobListView(ListView):
    model = JobListing
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    queryset = JobListing.objects.filter(is_active=True)

class JobDetailView(DetailView):
    model = JobListing
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = self.get_object()
        user = self.request.user
        
        has_applied = False
        is_owner = False
        
        if user.is_authenticated:
            if user.role == 'CANDIDATE':
                has_applied = Application.objects.filter(job=job, candidate=user).exists()
            elif user.role == 'RECRUITER':
                if job.posted_by == user:
                    is_owner = True
        
        context['has_applied'] = has_applied
        context['is_owner'] = is_owner
        return context

class JobCreateView(LoginRequiredMixin, RecruiterRequiredMixin, CreateView):
    model = JobListing
    template_name = 'jobs/job_form.html'
    fields = ['title', 'description', 'requirements', 'location']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class JobDeleteView(LoginRequiredMixin, JobOwnerRequiredMixin, DeleteView):
    model = JobListing
    template_name = 'jobs/job_confirm_delete.html'
    context_object_name = 'job'
    success_url = reverse_lazy('dashboard')

# 2. ADD THIS NEW VIEW CLASS
class JobUpdateView(LoginRequiredMixin, JobOwnerRequiredMixin, UpdateView):
    model = JobListing
    # We reuse the same form template from our create view
    template_name = 'jobs/job_form.html' 
    fields = ['title', 'description', 'requirements', 'location']
    context_object_name = 'job'
    success_url = reverse_lazy('dashboard')