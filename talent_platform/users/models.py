from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        CANDIDATE = 'CANDIDATE', 'Candidate'
        RECRUITER = 'RECRUITER', 'Recruiter'

    role = models.CharField(max_length=50, choices=Role.choices)