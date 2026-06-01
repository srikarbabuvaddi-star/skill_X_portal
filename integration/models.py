from django.db import models

class APIConnector(models.Model):
    service_name = models.CharField(max_length=100)
    webhook_endpoint = models.URLField()