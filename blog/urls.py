from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('articles', views.all_articles_list, name='all_articles_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('about', views.about, name='about'),
]
