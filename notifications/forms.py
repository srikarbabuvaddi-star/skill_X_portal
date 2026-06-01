from django import forms
from .models import LiveAlert

class LiveAlertForm(forms.ModelForm):
    class Meta: model = LiveAlert; fields = ['seen']