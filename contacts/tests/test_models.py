from django.test import TestCase
from contacts.models import CustomerRequest


class CustomerRequestModelTest(TestCase):
    def test_create_customer_request(self):
        request = CustomerRequest.objects.create(
            full_name='علی رضایی',
            email='ali@example.com',
            phone='09123456789',
            service_type='consulting',
            description='نیاز به مشاوره دارم'
        )

        self.assertEqual(request.full_name, 'علی رضایی')
        self.assertEqual(request.service_type, 'consulting')
        self.assertEqual(request.status, 'new')
        self.assertEqual(request.priority, 'medium')