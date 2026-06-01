from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:skill_id>/', views.submit_feedback, name='submit_feedback'),
]