from rest_framework import viewsets
from .serializers import financialSerializer
from financial.models import financialInvoices

from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import BasicAuthentication


class api_view(viewsets.ModelViewSet):
    serializer_class = financialSerializer
    queryset = financialInvoices.objects.all()
    
	#authentication_classes = (BasicAuthentication, )
    permission_classes = [IsAuthenticated]  # Requer autenticação para todas as ações
    #def get_queryset(self):
    #    return self.queryset.filter(user=self.request.user)