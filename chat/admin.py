from django.contrib import admin
from .models import MessagingRoom, SavedMessage
admin.site.register(MessagingRoom)
admin.site.register(SavedMessage)