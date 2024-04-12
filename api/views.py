from rest_framework import viewsets
from .serializers import financialSerializer
from financial.models import financialInvoices
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view


# docs
# -----------------------------------------------------------------
schema_view = get_schema_view(
    openapi.Info(
        title="Nectarinv - Financial and Investment API",
        default_version='v1.0.0',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# -----------------------------------------------------------------

# Financial routes
# -----------------------------------------------------------------
class financialApiView(viewsets.ModelViewSet):
    serializer_class = financialSerializer
    queryset = financialInvoices.objects.all()

    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# -----------------------------------------------------------------
