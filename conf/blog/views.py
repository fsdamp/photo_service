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


class ArticleDetailView(generics.RetrieveAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        HitCountMixin.hit_count(request, obj.hit_count)
        return super(ArticleDetailView, self).get(request, args, kwargs)
