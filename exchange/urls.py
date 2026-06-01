from django.urls import path
from . import views

urlpatterns = [
    path('propose/<int:receiver_id>/', views.trigger_proposal, name='trigger_proposal'),
    path('decide/<int:pk>/<str:decision>/', views.evaluate_proposal, name='evaluate_proposal'),
]