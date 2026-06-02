from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def integration_config_panel(request):
    return render(request, 'secure.html')
