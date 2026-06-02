from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import MessagingRoom, SavedMessage

@login_required
def chat_home(request):
    if request.method == 'POST':
        room_token = request.POST.get('room_token', '').strip()
        if room_token:
            MessagingRoom.objects.get_or_create(room_token=room_token)
            return redirect('access_chat_room', room_token=room_token)

    rooms = MessagingRoom.objects.all().order_by('room_token')
    recent_messages = SavedMessage.objects.select_related('room', 'author').order_by('-sent_at')[:10]
    return render(request, 'inbox.html', {'rooms': rooms, 'recent_messages': recent_messages})

@login_required
def access_chat_room(request, room_token):
    room, _ = MessagingRoom.objects.get_or_create(room_token=room_token)
    logs = room.messages.all().order_by('sent_at')
    return render(request, 'root.html', {'room_token': room_token, 'logs': logs})

@login_required
def chat_detail(request, message_id):
    message = get_object_or_404(SavedMessage, pk=message_id)
    return render(request, 'chat/detail.html', {'message': message})
