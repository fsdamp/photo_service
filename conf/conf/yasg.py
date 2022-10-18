from django.urls import include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from blog.urls import urlpatterns as urls

schema_view = get_schema_view(
    openapi.Info(
        title="Photo service",
        default_version='v1',

    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    patterns=[
        re_path(r'api/', include(urls)),
    ]

)
