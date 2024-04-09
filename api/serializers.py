from rest_framework import serializers
from financial.models import financialInvoices

class financialSerializer(serializers.ModelSerializer):
    class Meta:
        model = financialInvoices
        fields = '__all__'