from django.db import models
from django.contrib.auth.models import User

class TimetableSlot(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='slots_created')
    learner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='slots_booked')
    execution_date = models.DateField()
    time_bracket = models.CharField(max_length=100)