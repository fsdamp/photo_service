from django.shortcuts import render
from django_filters import rest_framework as filters

# Create your views here.
from rest_framework import views, permissions, viewsets, mixins, status, parsers, generics

from blog.filters import ArticlesListFilter
from blog.models import Article
from blog.serializers import ArticlesSerializer, ArticleDetailSerializer
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


class ArticlesView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    filter_backends = [ArticlesListFilter, ]

    def filter_queryset(self, queryset: Article.objects):
        if self.request.GET.get('order_by', 'new') == 'popular':
            return queryset.order_by('-hit_count_generic__hits')
        return queryset


class MainArticlesView(generics.ListAPIView):
    serializer_class = ArticlesSerializer
    pagination_class = None

    def get_queryset(self):
        new = Article.objects.exclude(is_main=True).order_by('-id')[:3]
        most_views = Article.objects.exclude(is_main=True, id__in=list(new.values_list('id', flat=True))).order_by('-hit_count_generic__hits')[:3]
        main = Article.objects.filter(is_main=True)
        return most_views | new | main


class ArticleDetailView(generics.RetrieveAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleDetailSerializer

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        HitCountMixin.hit_count(request, obj.hit_count)
        return super(ArticleDetailView, self).get(request, args, kwargs)
