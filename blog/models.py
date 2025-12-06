from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='دسته بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ', blank=True)
    content = models.TextField(verbose_name='محتوای مقاله')
    cover_image = models.ImageField(upload_to='blog/covers/', verbose_name='تصویر کاور', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    author = models.CharField(max_length=100, default='تیم پرتو تجسم', verbose_name='نویسنده')
    view_count = models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    is_published = models.BooleanField(default=False, verbose_name='منتشر شده')
    is_featured = models.BooleanField(default=False, verbose_name='مقاله ویژه')
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ انتشار')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
        ordering = ['-published_at', '-created_at']




class Comment(models.Model):
    RATING_CHOICES = [
        (1, '۱ ستاره'),
        (2, '۲ ستاره'),
        (3, '۳ ستاره'),
        (4, '۴ ستاره'),
        (5, '۵ ستاره'),
    ]

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    author_name = models.CharField(max_length=100, verbose_name='نام نویسنده')
    author_email = models.EmailField(verbose_name='ایمیل نویسنده')
    content = models.TextField(verbose_name='متن نظر')
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=5, verbose_name='امتیاز')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')
    is_approved = models.BooleanField(default=False, verbose_name='تایید شده')
    is_spam = models.BooleanField(default=False, verbose_name='اسپم')

    def __str__(self):
        return f'نظر {self.author_name} برای {self.blog.title}'

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
        ordering = ['-created_at']