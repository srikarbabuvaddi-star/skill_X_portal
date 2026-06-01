def platform_context(request):
    if request.user.is_authenticated:
    
        from accounts.models import RoleAssignment
        try:
            role_meta = RoleAssignment.objects.get(user=request.user)
            return {'USER_ROLE': role_meta.role}
        except RoleAssignment.DoesNotExist:
            return {'USER_ROLE': 'LEARNER'}
    return {'USER_ROLE': 'ANONYMOUS'}