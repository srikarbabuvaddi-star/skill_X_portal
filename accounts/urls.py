# accounts/urls.py
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dynamic_dashboard_router, name='dashboard'),
    path('course/create/', views.create_course, name='create_course'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('users/manage/', views.manage_users, name='manage_users'),
    path('user/create/', views.create_user, name='create_user'),
    path('courses/manage/', views.manage_courses, name='manage_courses'),
    path('settings/site/', views.site_settings, name='site_settings'),
    path('settings/roles/', views.manage_roles, name='manage_roles'),
    path('register/', views.register_user, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # skills URLs are included at the project root, avoid duplicate include here
]