from django.shortcuts import render, redirect
from .forms import CandidateSignUpForm, RecruiterSignUpForm

def signup_choice(request):
    return render(request, 'users/signup_choice.html')

def candidate_signup(request):
    if request.method == 'POST':
        form = CandidateSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page
            return redirect('login') 
    else:
        form = CandidateSignUpForm()
    return render(request, 'users/signup_form.html', {'form': form})

def recruiter_signup(request):
    if request.method == 'POST':
        form = RecruiterSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page
            return redirect('login')
    else:
        form = RecruiterSignUpForm()
    return render(request, 'users/signup_form.html', {'form': form})