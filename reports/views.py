from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ActivityMetric

@login_required
def user_activity_reports(request):
    logs = ActivityMetric.objects.filter(user=request.user).order_by('-timestamp')[:20]
    return render(request, 'tracker.html', {'logs': logs})

@login_required
def report_detail(request, pk):
    report = get_object_or_404(ActivityMetric, pk=pk)
    return render(request, 'detail.html', {'report': report})
