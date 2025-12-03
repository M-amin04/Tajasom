from rest_framework import viewsets
from .models import CustomerRequest
from .serializers import CustomerRequestSerializer
from .tasks import send_customer_request_notification


class CustomerRequestViewSet(viewsets.ModelViewSet):
    queryset = CustomerRequest.objects.all()
    serializer_class = CustomerRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_customer_request_notification.delay(instance.id)