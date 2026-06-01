from django.db import models
from django.contrib.auth.models import User

class LearningGroup(models.Model):
    title = models.CharField(max_length=200)
    about = models.TextField()
    members = models.ManyToManyField(User, related_name='learning_groups', blank=True)

    def __str__(self):
        return self.title