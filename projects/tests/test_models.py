from unittest import TestCase
from projects.models import Category, Project, ProjectImage


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(title='نفت')
        self.assertEqual(category.title, 'نفت')
        self.assertEqual(str(category), 'نفت')

    def test_category_max_length(self):
        category = Category(title='ن' * 101)
        with self.assertRaises(Exception):
            category.save()


class ProjectModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='ساختمان')

    def test_create_project(self):
        project = Project.objects.create(
            title='ساختمانی و اداری',
            description='ساختمان ۵ طبقه',
            category=self.category,
            status='finished'
        )
        self.assertEqual(project.title, 'ساختمانی و اداری')
        self.assertEqual(project.status, 'finished')
        self.assertTrue(project.is_active)

    def test_project_status_choices(self):
        project = Project(
            title='تست',
            description='تست',
            category=self.category,
            status='in_progress'
        )
        project.save()
        self.assertEqual(project.status, 'in_progress')


class ProjectImageModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='صنعتی')
        self.project = Project.objects.create(
            title='کارخانه',
            description='کارخانه فولاد',
            category=self.category
        )

    def test_create_project_image(self):
        image = ProjectImage.objects.create(
            project=self.project,
            title='تصویر نمای خارجی',
            order=1
        )
        self.assertEqual(image.title, 'تصویر نمای خارجی')
        self.assertEqual(image.project, self.project)