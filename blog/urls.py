from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('articles', views.all_articles_list, name='all_articles_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('about', views.about, name='about'),
    path('article/new', views.article_new, name='article_new'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('article/<int:pk>/delete/',
         views.article_delete,
         name='article_delete'),
    path('search', views.search, name='search')
]
