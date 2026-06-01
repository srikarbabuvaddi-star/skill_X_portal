from django.db import models
from django.contrib.auth.models import User
from skills.models import SkillNode

class PerformanceReview(models.Model):
    skill = models.ForeignKey(SkillNode, on_delete=models.CASCADE, related_name='ratings')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()