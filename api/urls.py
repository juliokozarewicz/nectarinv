from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import financialApiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'api'

router = DefaultRouter()
router.register(r'financial', financialApiView, basename='financialApiView')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]