from django import forms
from .models import TimetableSlot

class TimetableSlotForm(forms.ModelForm):
    class Meta: model = TimetableSlot; fields = ['execution_date', 'time_bracket']