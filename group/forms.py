from django import forms
from .models import LearningGroup

class LearningGroupForm(forms.ModelForm):
    class Meta:
        model = LearningGroup
        fields = ['title', 'about']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }