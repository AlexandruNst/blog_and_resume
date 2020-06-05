from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('articles', views.all_articles_list, name='all_articles_list')
]
