from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from skills.models import SkillNode
from .models import SwapProposal
from .forms import SwapProposalForm

@login_required
def exchange_dashboard(request):
    if request.method == 'POST':
        form = SwapProposalForm(request.POST)
        receiver_id = request.POST.get('receiver')
        if form.is_valid() and receiver_id:
            proposal = form.save(commit=False)
            proposal.sender = request.user
            proposal.receiver = get_object_or_404(User, pk=receiver_id)
            proposal.save()
            return redirect('exchange_dashboard')
    else:
        form = SwapProposalForm()

    users = User.objects.exclude(pk=request.user.pk).order_by('username')
    skills = SkillNode.objects.select_related('owner').order_by('title')
    sent = SwapProposal.objects.filter(sender=request.user).select_related('receiver', 'offered_skill', 'requested_skill')
    received = SwapProposal.objects.filter(receiver=request.user).select_related('sender', 'offered_skill', 'requested_skill')
    return render(request, 'exchange/dashboard.html', {
        'form': form,
        'users': users,
        'skills': skills,
        'sent': sent,
        'received': received,
    })

@login_required
def trigger_proposal(request, receiver_id):
    if request.method == "POST":
        SwapProposal.objects.create(
            sender=request.user,
            receiver_id=receiver_id,
            offered_skill_id=request.POST.get('offered'),
            requested_skill_id=request.POST.get('requested')
        )
    return redirect('dashboard')

@login_required
def evaluate_proposal(request, pk, decision):
    proposal = get_object_or_404(SwapProposal, pk=pk, receiver=request.user)
    proposal.status = 'ACCEPTED' if decision == 'accept' else 'REJECTED'
    proposal.save()
    return redirect('dashboard')
