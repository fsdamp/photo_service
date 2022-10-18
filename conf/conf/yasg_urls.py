from django.urls import path, include, re_path
from .yasg import schema_view

urlpatterns = [
    re_path(r'^swagger/api(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/api/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^swagger/api/docs/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),

]
