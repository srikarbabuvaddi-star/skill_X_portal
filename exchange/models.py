from django.db import models
from django.contrib.auth.models import User
from skills.models import SkillNode

class SwapProposal(models.Model):
    STATUS = [('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')]
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_proposals')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_proposals')
    offered_skill = models.ForeignKey(SkillNode, on_delete=models.CASCADE, related_name='offered_swaps')
    requested_skill = models.ForeignKey(SkillNode, on_delete=models.CASCADE, related_name='requested_swaps')
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')