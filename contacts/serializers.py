from rest_framework import serializers
from .models import CustomerRequest

class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = [
            'id', 'full_name', 'email', 'phone', 'company', 'service_type',
            'priority', 'title', 'description', 'status', 'created_at'
        ]
        read_only_fields = ['id', 'status', 'created_at']