from rest_framework import serializers
from .models import CompanyInfo, TeamMember, Client, CompanyHistory, CompanyContact


class CompanyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyHistory
        fields = ['id', 'year', 'title', 'description', 'image', 'order', 'is_active']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'position', 'bio', 'image', 'email', 'phone', 'order']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'logo', 'website', 'order']


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = [
            'id', 'name', 'description', 'mission', 'vision', 'values',
            'years_experience', 'completed_projects', 'happy_clients'
        ]


class CompanyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyContact
        fields = ['id', 'address', 'phone', 'email', 'working_hours']