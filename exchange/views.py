from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SwapProposal

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