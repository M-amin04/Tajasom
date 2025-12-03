from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerRequestViewSet

router = DefaultRouter()
router.register(r'customer-requests', CustomerRequestViewSet, basename='customer-requests')

urlpatterns = [
    path('', include(router.urls)),
]