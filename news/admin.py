from django.contrib import admin

# Register your models here.
# news/admin.py

from .models import Category, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date')
    list_filter = ('category', 'publication_date')
    search_fields = ('title', 'content')

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)