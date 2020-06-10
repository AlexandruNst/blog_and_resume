from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume, name='resume'),
    path('new', views.resume_new, name='resume_new'),
    path('<int:pk>/edit/', views.resume_edit, name='resume_edit'),
    path('<int:pk>/delete/', views.resume_delete, name='resume_delete'),
]
