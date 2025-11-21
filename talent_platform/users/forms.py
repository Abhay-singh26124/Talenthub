from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CandidateSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email') # You can add 'first_name', 'last_name' here too

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.CANDIDATE
        if commit:
            user.save()
        return user

class RecruiterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email') # You can add 'first_name', 'last_name' here too

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.RECRUITER
        if commit:
            user.save()
        return user