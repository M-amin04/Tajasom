from django.test import TestCase
from blog.models import Category, Blog, Comment
from blog.serializers import CategorySerializer, BlogSerializer, CommentSerializer


class CategorySerializerTest(TestCase):
    def test_serializer_valid_data(self):
        data = {'title': 'سبک زندگی'}
        serializer = CategorySerializer(data=data)
        self.assertTrue(serializer.is_valid())


class BlogSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='اقتصاد')

    def test_serializer_valid_data(self):
        data = {
            'title': 'مقاله اقتصادی',
            'content': 'تحلیل بازار',
            'category': self.category.id,
            'author': 'کارشناس اقتصادی'
        }
        serializer = BlogSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_returns_comments_count(self):
        blog = Blog.objects.create(
            title='تست',
            content='تست',
            category=self.category
        )
        Comment.objects.create(
            blog=blog,
            author_name='کاربر ۱',
            author_email='user1@example.com',
            content='نظر اول'
        )
        Comment.objects.create(
            blog=blog,
            author_name='کاربر ۲',
            author_email='user2@example.com',
            content='نظر دوم'
        )
        serializer = BlogSerializer(blog)
        self.assertEqual(serializer.data['comments_count'], 2)


class CommentSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='سیاست')
        self.blog = Blog.objects.create(
            title='مقاله سیاسی',
            content='محتوا',
            category=self.category
        )

    def test_serializer_valid_data(self):
        data = {
            'author_name': 'علی',
            'author_email': 'ali@example.com',
            'content': 'مقاله خوبی بود',
            'rating': 4
        }
        serializer = CommentSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_with_blog_context(self):
        data = {
            'author_name': 'رضا',
            'author_email': 'reza@example.com',
            'content': 'عالی',
            'rating': 5
        }
        serializer = CommentSerializer(data=data, context={'blog': self.blog})
        self.assertTrue(serializer.is_valid())