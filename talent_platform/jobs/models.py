from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'RECRUITER'} # Ensures only recruiters can post
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title