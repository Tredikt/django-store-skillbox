from rest_framework import serializers
from .models import Article, Tag, Author, Category




class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "name",
            "bio",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "name",
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "title",
            "content",
            "author",
            "category",
            "tags",
        )