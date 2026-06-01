from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_and_edit_profile, name='profile'),
    path('me/', views.view_and_edit_profile, name='view_and_edit_profile'),
]
