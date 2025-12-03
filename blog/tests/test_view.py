from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from blog.models import Blog, Category
from django.urls import reverse


class BlogViewCountTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(title='ورزش')
        self.blog = Blog.objects.create(
            title='اولین مقاله',
            content='محتوا',
            category=self.category,
            is_published=True,
            published_at=timezone.now()
        )

    def test_view_count_increments_on_retrieve(self):
        url = reverse('blog-posts-detail', args=[self.blog.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.blog.refresh_from_db()
        self.assertEqual(self.blog.view_count, 1)


class BlogAddCommentTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(title='ورزشی')
        self.blog = Blog.objects.create(
            title="دومین مقاله",
            content="محتوای دومین مقاله",
            category=self.category,
            is_published=True,
            published_at=timezone.now()
        )
        self.comment_data = {
            "author_name": "امین",
            "author_email": "amin@example.com",
            "content": "نظر تست",
            "rating": 4,
        }

    def test_add_comment_creates_comment(self):
        url = reverse('blog-posts-add-comment', args=[self.blog.id])
        response = self.client.post(url, self.comment_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(self.blog.comments.count(), 1)
        comment = self.blog.comments.first()
        self.assertEqual(comment.author_name, self.comment_data['author_name'])
        self.assertEqual(comment.is_approved, False)
        self.assertEqual(comment.blog.id, self.blog.id)
