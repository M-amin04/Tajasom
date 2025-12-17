from django.utils import timezone
from django.test import TestCase
from projects.models import Category, Project, ProjectImage
from projects.serializers import CategorySerializer, ProjectSerializer


class CategorySerializerTest(TestCase):
    def test_serializer_valid_date(self):
        ser = CategorySerializer(data={'title': 'پتروشیمی'})
        self.assertTrue(ser.is_valid())
        self.assertEqual(ser.validated_data['title'], 'پتروشیمی')

    def test_serializer_invalid_data(self):
        ser = CategorySerializer(data={'title': ''})
        self.assertFalse(ser.is_valid())
        self.assertIn('title', ser.errors)


class ProjectSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='انرژی')

    def test_serializer_valid_data(self):
        data = {
            'title': 'پروژه نیروگاه',
            'description': 'نیروگاه خورشیدی',
            'category': self.category.id,
            'status': 'in_progress',
            'project_date': '2024-01-15',
        }
        ser = ProjectSerializer(data=data)
        self.assertTrue(ser.is_valid())

    def test_serializer_return_images(self):
        project = Project.objects.create(
            title='تست',
            description='تست',
            category=self.category,
            project_date=timezone.now().date()
        )

        ProjectImage.objects.create(
            project=project,
            title='تصویر تست'
        )
        ser = ProjectSerializer(project)
        data = ser.data
        self.assertIn('images', data)

        self.assertIsInstance(data['images'], list)
        self.assertGreater(len(data['images']), 0)
        image_data = data['images'][0]
        expected_field = {'id', 'image', 'title', 'description', 'order', 'is_main'}

        for field in expected_field:
            self.assertIn(field, image_data)
