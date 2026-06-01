from django.urls import path
from . import views

urlpatterns = [
    path('vault/', views.materials_repository, name='materials_repository'),
]