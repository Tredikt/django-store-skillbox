from django.contrib.syndication.views import Feed
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Article, Author, Tag, Category, ArticleVideo
from .serializers import AuthorSerializer, CategorySerializer, TagSerializer, ArticleSerializer


class ArticlesListViewVideo(ListView):
    template_name = "blogapp/article_video_list.html"
    queryset = (
        ArticleVideo.objects
        .filter(published_at__isnull=False)
        .order_by("-published_at")
    )


class LatestArticlesFeed(Feed):
    title = "Blog articles (latest)"
    description = "Updates on changes and addition blog articles"
    link = reverse_lazy("blogapp:articles_video")

    def items(self):
        return (
            ArticleVideo.objects
            .filter(published_at__isnull=False)
            .order_by("-published_at")[:5]
        )

    def item_title(self, item: ArticleVideo):
        return item.title

    def item_description(self, item: ArticleVideo):
        return item.body[:200]


class ArticleDetailView(DetailView):
    model = ArticleVideo


class ArticlesListView(ListView):
    queryset = (
        Article.objects
        .select_related("author", "category")
        .prefetch_related("tags")
        .defer("content")
    )
    context_object_name = "articles"
    template_name = "blogapp/article_list.html"



class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



