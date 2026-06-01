from django import forms
from .models import LiveWorkshop

class LiveWorkshopForm(forms.ModelForm):
    class Meta:
        model = LiveWorkshop
        fields = ['topic', 'execution_time']
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'execution_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }