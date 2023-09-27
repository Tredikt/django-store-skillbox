from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ArticlesListView,
    AuthorViewSet,
    CategoryViewSet,
    TagViewSet,
    ArticleViewSet,
    ArticlesListViewVideo,
    ArticleDetailView,
    LatestArticlesFeed,
)

app_name = "blogapp"

routers = DefaultRouter()
routers.register("authors", AuthorViewSet)
routers.register("categories", CategoryViewSet)
routers.register("tags", TagViewSet)
routers.register("articles", ArticleViewSet)

urlpatterns = [
    path("articles_video/", ArticlesListViewVideo.as_view(), name="articles_video"),
    path("article_video/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("articles_video/latest/feed/", LatestArticlesFeed(), name="latest_feed"),
    path("articles/", ArticlesListView.as_view(), name="articles"),
    path("api/", include(routers.urls))
]