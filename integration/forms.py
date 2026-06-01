from django import forms
from .models import APIConnector

class APIConnectorForm(forms.ModelForm):
    class Meta: model = APIConnector; fields = '__all__'