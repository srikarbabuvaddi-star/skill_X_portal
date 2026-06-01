from django import forms
from .models import CourseMaterial

class CourseMaterialForm(forms.ModelForm):
    class Meta:
        model = CourseMaterial
        fields = ['title', 'resource_link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'resource_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }