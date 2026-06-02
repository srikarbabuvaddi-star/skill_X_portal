from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from skills.models import SkillNode
from .models import PerformanceReview

@login_required
def reviews_dashboard(request):
    reviews = PerformanceReview.objects.select_related('skill', 'reviewer').order_by('-id')
    skills = SkillNode.objects.select_related('owner').order_by('title')
    return render(request, 'reviews/dashboard.html', {'reviews': reviews, 'skills': skills})

@login_required
def submit_feedback(request, skill_id):
    if request.method == 'POST':
        node = get_object_or_404(SkillNode, id=skill_id)
        PerformanceReview.objects.create(
            skill=node,
            reviewer=request.user,
            score=int(request.POST.get('score')),
            comment=request.POST.get('comment')
        )
    return redirect('list_skills')
