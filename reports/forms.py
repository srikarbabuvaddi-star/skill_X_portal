from django import forms
from .models import ActivityMetric

class ActivityMetricForm(forms.ModelForm):
    class Meta: model = ActivityMetric; fields = ['action']