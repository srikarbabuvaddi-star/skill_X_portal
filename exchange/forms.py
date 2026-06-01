from django import forms
from .models import SwapProposal

class SwapProposalForm(forms.ModelForm):
    class Meta:
        model = SwapProposal
        fields = ['offered_skill', 'requested_skill']