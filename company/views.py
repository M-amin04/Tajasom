from rest_framework import viewsets
from .models import CompanyInfo, TeamMember, Client, CompanyHistory, CompanyContact
from .serializers import CompanyInfoSerializer, TeamMemberSerializer, ClientSerializer, CompanyHistorySerializer, \
    CompanyContactSerializer


class CompanyHistoryViewSet(viewsets.ModelViewSet):
    queryset = CompanyHistory.objects.filter(is_active=True)
    serializer_class = CompanyHistorySerializer
    ordering = ['order', 'year']


class CompanyInfoViewSet(viewsets.ModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer
    ordering = ['order']


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.filter(is_active=True)
    serializer_class = ClientSerializer
    ordering = ['order']



class CompanyContactViewSet(viewsets.ModelViewSet):
    queryset = CompanyContact.objects.all()
    serializer_class = CompanyContactSerializer