from django import forms

class CreditFundingForm(forms.Form):
    funding_value = forms.DecimalField(max_digits=6, decimal_places=2)