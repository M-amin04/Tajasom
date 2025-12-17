from django.test import TestCase
from django.utils import timezone
from blog.models import Category, Blog, Comment


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(title='تکنولوژی')
        self.assertEqual(category.title, 'تکنولوژی')
        self.assertEqual(str(category), 'تکنولوژی')


class BlogModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='ساخت و ساز')

    def test_create_blog(self):
        blog = Blog.objects.create(
            title='مقاله ساخت و ساز',
            content='محتوای مقاله',
            category=self.category,
            author='نویسنده تست'
        )
        self.assertEqual(blog.title, 'مقاله ساخت و ساز')
        self.assertEqual(blog.view_count, 0)
        self.assertFalse(blog.is_published)
        self.assertFalse(blog.is_featured)

    def test_blog_ordering(self):
        blog1 = Blog.objects.create(
            title='مقاله اول',
            content='محتوا',
            category=self.category,
            published_at=timezone.now()
        )
        blog2 = Blog.objects.create(
            title='مقاله دوم',
            content='محتوا',
            category=self.category,
            published_at=timezone.now() + timezone.timedelta(days=1)
        )
        blogs = Blog.objects.all()
        self.assertEqual(blogs[0], blog2)
        self.assertEqual(blogs[1], blog1)


class CommentModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='آموزش')
        self.blog = Blog.objects.create(
            title='مقاله آموزشی',
            content='محتوا',
            category=self.category
        )

    def test_create_comment(self):
        comment = Comment.objects.create(
            blog=self.blog,
            author_name='محمد',
            author_email='mohammad@example.com',
            content='مقاله عالی بود',
            rating=5
        )
        self.assertEqual(comment.author_name, 'محمد')
        self.assertEqual(comment.rating, 5)
        self.assertFalse(comment.is_approved)
        self.assertFalse(comment.is_spam)