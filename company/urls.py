from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyHistoryViewSet, CompanyInfoViewSet, TeamMemberViewSet, ClientViewSet

router = DefaultRouter()
router.register(r'history', CompanyHistoryViewSet, basename='history')
router.register(r'info', CompanyInfoViewSet, basename='company-info')
router.register(r'team', TeamMemberViewSet, basename='team-members')
router.register(r'clients', ClientViewSet, basename='clients')

urlpatterns = [
    path('', include(router.urls)),
]