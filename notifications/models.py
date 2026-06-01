from django.db import models
from django.contrib.auth.models import User

class LiveAlert(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts')
    body = models.CharField(max_length=255)
    seen = models.BooleanField(default=False)