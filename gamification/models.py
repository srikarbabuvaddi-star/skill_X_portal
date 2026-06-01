from django.db import models
from django.contrib.auth.models import User

class UserXpLedger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='xp_ledger')
    points = models.IntegerField()
    event_reason = models.CharField(max_length=255)
    awarded_at = models.DateTimeField(auto_now_add=True)