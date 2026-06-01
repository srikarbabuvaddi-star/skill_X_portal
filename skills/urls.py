from django.urls import path
from . import views 

urlpatterns = [
    path('', views.list_skills, name='list_skills'),
    path('', views.list_skills, name='skill_list'),
    path('home/', views.home, name='home'),
    path('progress/', views.progress, name='progress'),
    path('tracker/', views.tracker, name='tracker'),
    path('share/', views.share, name='share'),
    path('add/', views.create_skill, name='create_skill'),
    path('addskill/', views.addskill, name='addskill'),
    path('detail/<int:pk>/', views.skill_detail, name='skill_detail'),
    path('<int:pk>/edit/', views.edit_skill, name='edit_skill'),
    path('<int:pk>/delete/', views.delete_skill, name='delete_skill'),
]
