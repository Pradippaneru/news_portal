# news/views.py
from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def home_page(request):
    # गृह पृष्ठको लागि सबैभन्दा नयाँ ५ वटा समाचार देखाउने
    latest_articles = Article.objects.all()[:5]
    categories = Category.objects.all()
    context = {
        'articles': latest_articles,
        'categories': categories,
    }
    return render(request, 'news/home.html', context)

def category_page(request, category_id):
    # श्रेणी अनुसार समाचार देखाउने
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'articles': articles,
        'categories': categories,
    }
    return render(request, 'news/category.html', context)

def article_detail(request, article_id):
    # एउटा समाचारको पूरा विवरण देखाउने
    article = get_object_or_404(Article, id=article_id)
    categories = Category.objects.all()
    context = {
        'article': article,
        'categories': categories,
    }
    return render(request, 'news/article_detail.html', context)