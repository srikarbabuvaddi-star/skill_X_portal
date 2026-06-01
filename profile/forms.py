from django import forms
from .models import ProfileMetadata

class ProfileMetadataForm(forms.ModelForm):
    class Meta: model = ProfileMetadata; fields = ['biography', 'avatar_link']