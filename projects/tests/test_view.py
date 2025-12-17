from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from projects.models import Category, Project



class ProjectViewSetTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='نفت')
        self.project = Project.objects.create(
            title='پروژه پالایشگاه',
            description='پالایشگاه نفت',
            category=self.category,
            is_active=True
        )

    def test_get_projects_list(self):
        url = reverse('projects-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project_detail(self):
        url = reverse('projects-detail', args=[self.project.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'پروژه پالایشگاه')

    def test_filter_by_category(self):
        url = f'{reverse('projects-list')}?category={self.category.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)