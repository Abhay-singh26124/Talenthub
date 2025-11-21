from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models

class CandidateProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        limit_choices_to={'role': 'CANDIDATE'} # Ensures only candidates have profiles
    )
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=500, blank=True, help_text="Comma-separated skills (e.g., Python, Sales, Marketing)")
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.user.username