from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LiveAlert

@login_required
def alert_inbox(request):
    pings = LiveAlert.objects.filter(recipient=request.user).order_by('-id')
    return render(request, 'notifications/inbox.html', {'pings': pings})