from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture_path = models.CharField(max_length=255, blank=True)  # Store file path as a string
    phone = models.CharField(max_length=15, blank=True)  # Additional field for phone number

    def __str__(self):
        return self.username
