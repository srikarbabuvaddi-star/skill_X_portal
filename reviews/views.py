from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from skills.models import SkillNode
from .models import PerformanceReview

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