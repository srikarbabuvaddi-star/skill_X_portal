from django import forms

class DynamicSearchForm(forms.Form):
    q = forms.CharField(max_length=200, required=False)