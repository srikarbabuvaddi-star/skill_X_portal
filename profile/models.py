from django.db import models
from django.contrib.auth.models import User

class ProfileMetadata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='metadata')
    biography = models.TextField(blank=True)
    avatar_link = models.URLField(default="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&h=150&q=80")