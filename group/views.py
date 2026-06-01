from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import LearningGroup

@login_required
def list_groups(request):
    hubs = LearningGroup.objects.all()
    return render(request, 'group/list.html', {'hubs': hubs})

@login_required
def join_group(request, pk):
    hub = get_object_or_404(LearningGroup, pk=pk)
    hub.members.add(request.user)
    return redirect('list_groups')