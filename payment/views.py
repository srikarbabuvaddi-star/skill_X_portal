from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StripeBillRecord

@login_required
def execute_funding_intent(request):
    if request.method == 'POST':
        StripeBillRecord.objects.create(
            user=request.user,
            charge_token="ch_mock_skill_x_asset",
            value_amount=float(request.POST.get('funding_value'))
        )
        return redirect('funding_success')
    return render(request, 'payment/checkout.html')

@login_required
def funding_success(request):
    return render(request, 'payment/success.html')