from django.urls import path
from . import views

urlpatterns = [
    path('timeline/', views.workshop_timeline, name='workshop_timeline'),
    path('create/', views.workshop_timeline, name='create_workshop'),
]
