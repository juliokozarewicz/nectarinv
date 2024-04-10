from rest_framework import viewsets
from .serializers import financialSerializer
from financial.models import financialInvoices
from rest_framework.permissions import IsAuthenticated


class api_view(viewsets.ModelViewSet):
    serializer_class = financialSerializer
    queryset = financialInvoices.objects.all()
    permission_classes = [IsAuthenticated]
