from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from skills.models import SkillNode

@login_required
def dynamic_search_engine(request):
    term = request.GET.get('q', '')
    matches = SkillNode.objects.filter(title__icontains=term) if term else SkillNode.objects.all()
    return render(request, 'index.html', {'matches': matches, 'term': term})