from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.execute_funding_intent, name='execute_funding_intent'),
    path('success/', views.funding_success, name='funding_success'),
]