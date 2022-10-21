from rest_framework import serializers

from blog.models import Article


class ArticlesSerializer(serializers.ModelSerializer):
    views_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    @staticmethod
    def get_views_count(obj):
        return obj.hit_count.hits


class ArticleDetailSerializer(serializers.ModelSerializer):
    views_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    @staticmethod
    def get_views_count(obj):
        return obj.hit_count.hits
