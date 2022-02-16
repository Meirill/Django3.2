from django.contrib import admin
from articles.models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)

# admin.site.register(Article)
