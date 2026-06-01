from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum

@login_required
def global_scoreboard(request):
    leaders = User.objects.annotate(total_xp=Sum('xp_ledger__points')).order_by('-total_xp')[:10]
    return render(request, 'board.html', {'leaders': leaders})