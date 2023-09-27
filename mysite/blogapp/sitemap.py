from django.contrib.sitemaps import Sitemap

from .models import ArticleVideo


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ArticleVideo.objects.filter(published_at__isnull=False).order_by("-published_at")

    def lastmod(self, obj: ArticleVideo):
        return obj.published_at