from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume, name='resume'),
    path('new', views.resume_new, name='resume_new'),
]
