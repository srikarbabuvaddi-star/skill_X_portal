from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ExtendedRegistrationForm
from .models import RoleAssignment

def register_user(request):
    if request.method == 'POST':
        form = ExtendedRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            RoleAssignment.objects.create(user=user, role=form.cleaned_data['role'])
            login(request, user)
            return redirect('dashboard')
    else:
        form = ExtendedRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dynamic_dashboard_router(request):
    # role_meta, _ = RoleAssignment.objects.get_or_create(user=request.user, defaults={'role': 'LEARNER'})
    # if role_meta.role == 'ADMIN':
    #     return render(request, 'dashboard/admin_dashboard.html')
    # elif role_meta.role == 'PROVIDER':
    #     return render(request, 'dashboard/provider_dashboard.html')
    return render(request, 'dashboard/learner_dashboard.html')

@login_required
def create_course(request):
    return render(request, 'course_create.html')

@login_required
def course_detail(request, pk):
    return render(request, 'course_detail.html', {'course_id': pk})

@login_required
def create_user(request):
    return render(request, 'create_user.html')

@login_required
def manage_courses(request):
    return render(request, 'manage_courses.html')

@login_required
def manage_users(request):
    return render(request, 'manage_users.html')

@login_required
def site_settings(request):
    return render(request, 'site_settings.html')

@login_required
def manage_roles(request):
    return render(request, 'manage_roles.html')
