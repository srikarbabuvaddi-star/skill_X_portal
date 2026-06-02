import uuid

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import VideoConference

@login_required
def video_home(request):
    if request.method == 'POST':
        uid = request.POST.get('uid', '').strip() or uuid.uuid4().hex[:12]
        session, _ = VideoConference.objects.get_or_create(
            uid=uid,
            defaults={'initializer': request.user},
        )
        return redirect('launch_video_ui', uid=session.uid)

    sessions = VideoConference.objects.select_related('initializer').order_by('uid')
    return render(request, 'video/home.html', {'sessions': sessions})

@login_required
def launch_video_ui(request, uid):
    session, _ = VideoConference.objects.get_or_create(
        uid=uid,
        defaults={'initializer': request.user},
    )
    return render(request, 'room.html', {'session': session})
