from django.conf import settings
from django.db import models
from jobs.models import JobListing

class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Under Review', 'Under Review'),
        ('Interview', 'Interview'),
        ('Hired', 'Hired'),
        ('Rejected', 'Rejected'),
    ]

    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applications',
        limit_choices_to={'role': 'CANDIDATE'}
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # A candidate can only apply to the same job once
        unique_together = ('job', 'candidate')

    def __str__(self):
        return f'{self.candidate.username} for {self.job.title}'