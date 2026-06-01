from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import VideoConference

@login_required
def launch_video_ui(request, uid):
    session = get_object_or_404(VideoConference, uid=uid)
    return render(request, 'room.html', {'session': session})