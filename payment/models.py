from django.db import models
from django.contrib.auth.models import User

class StripeBillRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    charge_token = models.CharField(max_length=255)
    value_amount = models.DecimalField(max_digits=8, decimal_places=2)