from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import financialApiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view


app_name = 'api'

router = DefaultRouter()
router.register(r'financial', financialApiView, basename='financialApiView')

schema_view = get_schema_view(
    openapi.Info(
        title="Nectarinv - Financial and Investment API",
        default_version='v1.0.0',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]