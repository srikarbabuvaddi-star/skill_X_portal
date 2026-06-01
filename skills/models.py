from django.db import models
from django.contrib.auth.models import User

class SkillNode(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills_provided')
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.title