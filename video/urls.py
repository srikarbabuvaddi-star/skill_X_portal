from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_home, name='video_home'),
    path('stream/<str:uid>/', views.launch_video_ui, name='launch_video_ui'),
]
