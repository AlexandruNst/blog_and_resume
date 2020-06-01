from django.shortcuts import render
from django.utils import timezone
from .models import Article


def post_list(request):
    articles = Article.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'articles': articles})
