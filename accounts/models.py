# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class RoleAssignment(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'), 
        ('LEARNER', 'Learner'), 
        ('PROVIDER', 'Provider')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='role_data')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='LEARNER')

    def __str__(self): 
        return f"{self.user.username} - {self.role}"