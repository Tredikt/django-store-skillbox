from django.contrib import admin

from .models import ArticleVideo


@admin.register(ArticleVideo)
class ArticleAdmin(admin.ModelAdmin):
    list_display = "id", "title", "body", "published_at"
