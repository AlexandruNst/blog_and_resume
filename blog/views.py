from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article


def post_list(request):
    articles = Article.objects.order_by('-created_date')
    featured_article = articles[0]
    side_articles = articles[1:5]
    return render(
        request, 'blog/featured.html', {
            'articles': articles,
            'featured_article': featured_article,
            'side_articles': side_articles
        })


def all_articles_list(request):
    articles = Article.objects.order_by('-created_date')
    return render(request, 'blog/all_articles.html', {
        'articles': articles,
    })


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    articles = Article.objects.order_by('-created_date')
    recommended_articles = [a for a in articles if a != article][:2]
    return render(request, 'blog/article_detail.html', {
        'article': article,
        'recommended_articles': recommended_articles
    })
