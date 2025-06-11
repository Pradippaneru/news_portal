# news/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('category/<int:category_id>/', views.category_page, name='category_page'),
]