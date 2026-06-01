from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TimetableSlot

@login_required
def calendar_matrix(request):
    if request.method == 'POST':
        TimetableSlot.objects.create(
            provider=request.user,
            execution_date=request.POST.get('date'),
            time_bracket=request.POST.get('bracket')
        )
        return redirect('calendar_matrix')
    open_slots = TimetableSlot.objects.filter(learner__isnull=True)
    return render(request, 'matrix.html', {'slots': open_slots})