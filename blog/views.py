from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def post_list(request):
    articles = Article.objects.order_by('-created_date')
    if len(articles) >= 5:
        featured_article = articles[0]
        side_articles = articles[1:5]
        return render(
            request, 'blog/featured.html', {
                'articles': articles,
                'featured_article': featured_article,
                'side_articles': side_articles
            })
    else:
        return render(request, 'blog/base_nav_footer.html')


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


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    if request.GET.get('q'):
        query = request.GET.get('q')
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
            | Q(text__icontains=query)).order_by('-created_date')
        return render(request, 'blog/all_articles.html', {
            'articles': articles,
        })
    else:
        tag = request.GET.get('t')
        articles = Article.objects.filter(tags__icontains=tag)
        return render(request, 'blog/all_articles.html', {
            'articles': articles,
        })


@login_required
def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('all_articles_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/new_article.html', {'form': form})


@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('all_articles_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/new_article.html', {'form': form})


@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect("all_articles_list")