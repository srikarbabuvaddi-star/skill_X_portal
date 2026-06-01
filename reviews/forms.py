from django import forms
from .models import PerformanceReview

class PerformanceReviewForm(forms.ModelForm):
    class Meta: model = PerformanceReview; fields = ['score', 'comment']