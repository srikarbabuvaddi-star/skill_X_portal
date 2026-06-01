from django.urls import path
from . import views

urlpatterns = [
    path('room/<str:room_token>/', views.access_chat_room, name='access_chat_room'),
    path('message/<int:message_id>/', views.chat_detail, name='chat_detail'),
]
