from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LiveWorkshop
from .forms import LiveWorkshopForm

@login_required
def workshop_timeline(request):
    if request.method == 'POST':
        form = LiveWorkshopForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('workshop_timeline')
    else:
        form = LiveWorkshopForm()
    events = LiveWorkshop.objects.all().order_by('execution_time')
    return render(request, 'timeline.html', {'events': events, 'form': form})