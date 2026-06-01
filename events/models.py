from django.db import models
from django.contrib.auth.models import User

class LiveWorkshop(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_workshops')
    topic = models.CharField(max_length=255)
    execution_time = models.DateTimeField()

    def __str__(self):
        return self.topic