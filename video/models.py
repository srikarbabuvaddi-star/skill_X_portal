from django.db import models
from django.contrib.auth.models import User

class VideoConference(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    initializer = models.ForeignKey(User, on_delete=models.CASCADE)