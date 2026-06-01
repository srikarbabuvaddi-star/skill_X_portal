from django.urls import path
from . import views

urlpatterns = [
    path('config/', views.integration_config_panel, name='integration_config_panel'),
]