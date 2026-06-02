from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ExtendedRegistrationForm
from .models import RoleAssignment

APP_CARDS = [
    {
        "title": "Events",
        "description": "Track workshops and live timelines.",
        "icon": "bi-lightning-charge",
        "url_name": "workshop_timeline",
        "available": True,
    },
    {
        "title": "Resources",
        "description": "Open the course material vault.",
        "icon": "bi-folder2-open",
        "url_name": "materials_repository",
        "available": True,
    },
    {
        "title": "Reports",
        "description": "Review activity logs and analytics.",
        "icon": "bi-bar-chart-line",
        "url_name": "user_activity_reports",
        "available": True,
    },
    {
        "title": "Search",
        "description": "Run platform-wide discovery.",
        "icon": "bi-search",
        "url_name": "dynamic_search_engine",
        "available": True,
    },
    {
        "title": "Notifications",
        "description": "Read your platform alerts.",
        "icon": "bi-bell-fill",
        "url_name": "alert_inbox",
        "available": True,
    },
    {
        "title": "Integration",
        "description": "Configure external connections.",
        "icon": "bi-plug",
        "url_name": "integration_config_panel",
        "available": True,
    },
    {
        "title": "Profile",
        "description": "View and edit your account profile.",
        "icon": "bi-person-circle",
        "url_name": "view_and_edit_profile",
        "available": True,
    },
    {
        "title": "Payment",
        "description": "Open the checkout workflow.",
        "icon": "bi-credit-card",
        "url_name": "execute_funding_intent",
        "available": True,
    },
    {
        "title": "Chat",
        "description": "Open rooms and start conversations.",
        "icon": "bi-chat-dots",
        "url_name": "chat_home",
        "available": True,
    },
    {
        "title": "Video",
        "description": "Create and join video sessions.",
        "icon": "bi-camera-video",
        "url_name": "video_home",
        "available": True,
    },
    {
        "title": "Exchange",
        "description": "Send and manage skill swaps.",
        "icon": "bi-arrow-left-right",
        "url_name": "exchange_dashboard",
        "available": True,
    },
    {
        "title": "Reviews",
        "description": "Review feedback across skills.",
        "icon": "bi-star-half",
        "url_name": "reviews_dashboard",
        "available": True,
    },
]

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
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dynamic_dashboard_router(request):
    # role_meta, _ = RoleAssignment.objects.get_or_create(user=request.user, defaults={'role': 'LEARNER'})
    # if role_meta.role == 'ADMIN':
    #     return render(request, 'dashboard/admin_dashboard.html')
    # elif role_meta.role == 'PROVIDER':
    #     return render(request, 'dashboard/provider_dashboard.html')
    return render(request, 'dashboard/learner_dashboard.html', {'app_cards': APP_CARDS})

@login_required
def create_course(request):
    return render(request, 'accounts/course_create.html')

@login_required
def course_detail(request, pk):
    return render(request, 'accounts/course_detail.html', {'course_id': pk})

@login_required
def create_user(request):
    return render(request, 'accounts/create_user.html')

@login_required
def manage_courses(request):
    return render(request, 'accounts/manage_courses.html')

@login_required
def manage_users(request):
    return render(request, 'accounts/manage_users.html')

@login_required
def site_settings(request):
    return render(request, 'accounts/site_settings.html')

@login_required
def manage_roles(request):
    return render(request, 'accounts/manage_roles.html')
