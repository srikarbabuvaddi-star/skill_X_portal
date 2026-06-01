from django.db import models
from django.contrib.auth.models import User

class MessagingRoom(models.Model):
    room_token = models.CharField(max_length=255, unique=True)

class SavedMessage(models.Model):
    room = models.ForeignKey(MessagingRoom, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)