from django import forms
from .models import SavedMessage

class SavedMessageForm(forms.ModelForm):
    class Meta:
        model = SavedMessage
        fields = ['content']