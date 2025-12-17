from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone
from blog.models import Category, Blog, Comment
from django.contrib.auth.models import User


class BlogViewSetTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(title='تکنولوژی')
        self.blog = Blog.objects.create(
            title='مقاله تست',
            content='این یک مقاله تست است',
            category=self.category,
            is_published=True,
            published_at=timezone.now()
        )

    def test_get_blogs_list(self):
        url = reverse('blog-posts-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_blog_detail(self):
        url = reverse('blog-posts-detail', args=[self.blog.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.view_count, 1)

    def test_filter_by_category(self):
        url = f"{reverse('blog-posts-list')}?category_id={self.category.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_comment_to_blog(self):
        url = reverse('blog-posts-add-comment', args=[self.blog.id])
        data = {
            'author_name': 'امین',
            'author_email': 'amin@example.com',
            'content': 'مقاله مفیدی بود',
            'rating': 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.blog.comments.count(), 1)
        comment = self.blog.comments.first()
        self.assertEqual(comment.author_name, 'امین')

    def test_get_related_posts(self):
        Blog.objects.create(
            title='مقاله مرتبط',
            content='محتوا',
            category=self.category,
            is_published=True
        )
        url = reverse('blog-posts-related-posts', args=[self.blog.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CommentViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.category = Category.objects.create(title='آموزش')
        self.blog = Blog.objects.create(
            title='مقاله آموزشی',
            content='محتوا',
            category=self.category,
            is_published=True
        )
        self.comment = Comment.objects.create(
            blog=self.blog,
            author_name='سارا',
            author_email='sara@example.com',
            content='مقاله عالی',
            rating=5,
            is_approved=True
        )

    def test_get_comments_list(self):
        url = reverse('blog-comments-list')
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 403])

    def test_create_comment(self):
        url = reverse('blog-comments-list')
        data = {
            'author_name': 'محمد',
            'author_email': 'mohammad@example.com',
            'content': 'نظر تستی',
            'rating': 4,
            'blog': self.blog.id
        }
        response = self.client.post(url, data, format='json')
        self.assertIn(response.status_code, [201, 403])