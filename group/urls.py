from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_groups, name='list_groups'),
    path('join/<int:pk>/', views.join_group, name='join_group'),
]