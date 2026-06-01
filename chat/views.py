from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MessagingRoom, SavedMessage

@login_required
def access_chat_room(request, room_token):
    room, _ = MessagingRoom.objects.get_or_create(room_token=room_token)
    logs = room.messages.all().order_by('sent_at')
    return render(request, 'root.html', {'room_token': room_token, 'logs': logs})

@login_required
def chat_detail(request, message_id):
    message = get_object_or_404(SavedMessage, pk=message_id)
    return render(request, 'detail.html', {'message': message})
