from django import forms
from .models import SkillNode

class SkillNodeForm(forms.ModelForm):
    class Meta:
        model = SkillNode
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }