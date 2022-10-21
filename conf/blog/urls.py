from django.urls import path
from blog import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'api_customer_v1'

urlpatterns = [
    path('articles/', views.ArticlesView.as_view()),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view()),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
