from django.urls import path
from . import views

urlpatterns = [
    path('logs/', views.user_activity_reports, name='user_activity_reports'),
    path('detail/<int:pk>/', views.report_detail, name='report_detail'),
]
