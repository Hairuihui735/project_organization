from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('tariffs/', views.tariffs, name='tariffs'),
    path('leaders/', views.leaders, name='leaders'),
    path('become_client/', views.become_client, name='become_client'),
    path('accounts/profile/', views.profile, name='profile'),
    path('add_project/', views.add_project, name='add_project'),
    path('consultation_queue/', views.consultation_queue, name='consultation_queue'),
    path('consultation_queue/<int:pk>/', views.consultation_detail, name='consultation_detail'),
]