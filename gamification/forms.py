from django import forms
from .models import UserXpLedger

class UserXpLedgerForm(forms.ModelForm):
    class Meta: model = UserXpLedger; fields = ['points', 'event_reason']