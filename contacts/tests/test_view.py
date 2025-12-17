from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from contacts.models import CustomerRequest
from unittest.mock import patch


class CustomerRequestViewSetTest(APITestCase):
    def setUp(self):
        self.request = CustomerRequest.objects.create(
            full_name='رضا کریمی',
            email='reza@example.com',
            phone='09123456789',
            service_type='maquette',
            description='ماکت نیاز دارم'
        )

    def test_get_requests_list(self):
        url = reverse('customer-requests-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_request_detail(self):
        url = reverse('customer-requests-detail', args=[self.request.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('contacts.views.send_customer_request_notification.delay')
    def test_create_request(self, mock_task):
        url = reverse('customer-requests-list')
        data = {
            'full_name': 'نوید محمدی',
            'email': 'navid@example.com',
            'phone': '09129876543',
            'service_type': 'shipping',
            'description': 'ارسال بین‌المللی می‌خواهم'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomerRequest.objects.count(), 2)
        mock_task.assert_called_once()

    def test_filter_by_status(self):
        url = f"{reverse('customer-requests-list')}?status=new"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)