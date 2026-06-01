from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/', views.global_scoreboard, name='global_scoreboard'),
]