from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from company.models import CompanyHistory, TeamMember, CompanyInfo, Client


class CompanyHistoryViewSetTest(APITestCase):
    def setUp(self):
        self.history = CompanyHistory.objects.create(
            year='1399',
            title='اولین پروژه',
            description='پروژه اول انجام شد'
        )

    def test_get_history_list(self):
        url = reverse('history-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_history_detail(self):
        url = reverse('history-detail', args=[self.history.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamMemberViewSetTest(APITestCase):
    def setUp(self):
        self.member = TeamMember.objects.create(
            name='مریم کریمی',
            position='مدیر پروژه'
        )

    def test_get_team_list(self):
        url = reverse('team-members-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_team_detail(self):
        url = reverse('team-members-detail', args=[self.member.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CompanyInfoViewSetTest(APITestCase):
    def setUp(self):
        self.info = CompanyInfo.objects.create(
            name='شرکت مهندسی تجسم',
            description='تخصص در پروژه‌های نفت و گاز'
        )

    def test_get_company_info(self):
        url = reverse('company-info-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ClientViewSetTest(APITestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(
            name='شرکت پتروشیمی'
        )

    def test_get_clients_list(self):
        url = reverse('clients-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_client_detail(self):
        url = reverse('clients-detail', args=[self.client_obj.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)