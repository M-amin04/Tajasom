from django.test import TestCase
from company.serializers import (
    CompanyHistorySerializer, CompanyInfoSerializer,
    CompanyContactSerializer, TeamMemberSerializer, ClientSerializer
)


class SimpleSerializerTests(TestCase):
    def test_history_serializer(self):
        data = {'year': '1400', 'title': 'تاسیس', 'description': 'تاسیس شد'}
        serializer = CompanyHistorySerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_company_info_serializer(self):
        data = {'name': 'شرکت', 'description': 'توضیحات'}
        serializer = CompanyInfoSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_contact_serializer(self):
        data = {
            'address': 'تهران',
            'phone': '021-12345678',
            'email': 'info@test.com',
            'working_hours': '8-17'
        }
        serializer = CompanyContactSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_team_member_serializer_validation(self):
        data = {'name': 'علی', 'position': 'مهندس'}
        serializer = TeamMemberSerializer(data=data)
        self.assertIsNotNone(serializer.is_valid())

    def test_client_serializer_validation(self):
        data = {'name': 'مشتری'}
        serializer = ClientSerializer(data=data)
        self.assertIsNotNone(serializer.is_valid())