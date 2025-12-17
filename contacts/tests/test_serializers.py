from django.test import TestCase
from contacts.serializers import CustomerRequestSerializer


class CustomerRequestSerializerTest(TestCase):
    def test_serializer_valid_data(self):
        data = {
            'full_name': 'محمد احمدی',
            'email': 'mohammad@example.com',
            'phone': '09129876543',
            'service_type': 'design',
            'description': 'طراحی می‌خواهم'
        }

        serializer = CustomerRequestSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_email(self):
        data = {
            'full_name': 'تست',
            'email': 'invalid-email',
            'phone': '09123456789',
            'service_type': 'consulting',
            'description': 'تست'
        }

        serializer = CustomerRequestSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)