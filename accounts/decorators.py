from django.shortcuts import redirect
from functools import wraps

def provider_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        
        from accounts.models import RoleAssignment 
        
        try:
            role_meta = RoleAssignment.objects.get(user=request.user)
            if role_meta.role == 'PROVIDER' or request.user.is_superuser:
                return view_func(request, *args, **kwargs)
        except RoleAssignment.DoesNotExist:
            pass
            
        return redirect('dashboard')
    return _wrapped_view