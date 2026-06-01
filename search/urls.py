from django.urls import path
from . import views

urlpatterns = [
    path('run/', views.dynamic_search_engine, name='dynamic_search_engine'),
]