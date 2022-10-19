from django.shortcuts import render
from django_filters import rest_framework as filters

# Create your views here.
from rest_framework import views, permissions, viewsets, mixins, status, parsers, generics

from blog.models import Article
from blog.serializers import ArticlesSerializer, ArticleDetailSerializer
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


class ArticlesView(generics.ListAPIView):
    """
    you can sort articles via popularity and newest
    """
    # permission_classes = (permissions.AllowAny,)
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer

    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('is_new', 'is_popular')

    def get_ordering(self):
        ordering = self.request.GET.get('order_by', 'new')
        if ordering == 'popular':
            return 'hit_count_generic__hits'
        return ordering


class ArticleDetailView(generics.RetrieveAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        HitCountMixin.hit_count(request, obj.hit_count)
        return super(ArticleDetailView, self).get(request, args, kwargs)
