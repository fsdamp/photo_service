from rest_framework import serializers

from blog.models import Article


class ArticlesSerializer(serializers.ModelSerializer):
    views = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'poster', 'desc_h2', 'views', 'created_at')

    @staticmethod
    def get_views(obj):
        return obj.hit_count.hits


class ArticleDetailSerializer(serializers.ModelSerializer):
    views = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    @staticmethod
    def get_views(obj):
        return obj.hit_count.hits
