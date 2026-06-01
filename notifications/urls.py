from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.alert_inbox, name='alert_inbox'),
]