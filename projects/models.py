from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

class Project(models.Model):
    STATUS_CHOICES = [
        ('finished', 'تکمیل شده'),
        ('in_progress', 'در حال اجرا'),
        ('planned', 'برنامه‌ریزی شده'),
    ]

    title = models.CharField(max_length=200, verbose_name='عنوان پروژه')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ', blank=True)
    description = models.TextField(verbose_name='توضیحات')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed', verbose_name='وضعیت')
    image = models.ImageField(upload_to='projects/main/', verbose_name='تصویر', null=True, blank=True)
    client_name = models.CharField(max_length=100, blank=True, verbose_name='نام کارفرما')
    project_date = models.DateField(default=timezone.now, verbose_name='تاریخ پروژه')
    location = models.CharField(max_length=100, blank=True, verbose_name='موقعیت')
    duration = models.CharField(max_length=50, blank=True, verbose_name='مدت زمان اجرا')
    scale = models.CharField(max_length=50, blank=True, verbose_name='مقیاس')
    materials = models.TextField(blank=True, verbose_name='مواد به کار رفته')
    special_features = models.TextField(blank=True, verbose_name='ویژگی‌های خاص')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')
    is_featured = models.BooleanField(default=False, verbose_name='پروژه ویژه')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'
        ordering = ['order', '-created_at']


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name='پروژه')
    image = models.ImageField(upload_to='projects/gallery/', verbose_name='تصویر')
    title = models.CharField(max_length=100, blank=True, verbose_name='عنوان تصویر')
    description = models.TextField(blank=True, verbose_name='توضیحات تصویر')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')
    is_main = models.BooleanField(default=False, verbose_name='تصویر اصلی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f'{self.project.title} - {self.title}'

    class Meta:
        verbose_name = 'تصویر پروژه'
        verbose_name_plural = 'تصاویر پروژه'
        ordering = ['order', 'created_at']
