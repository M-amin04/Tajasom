from django.db import models

class CustomerRequest(models.Model):
    SERVICE_CHOICES = [
        ('maquette', 'ماکت‌سازی'),
        ('consulting', 'مشاوره'),
        ('shipping', 'ارسال بین‌المللی'),
        ('design', 'طراحی'),
        ('other', 'سایر'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'کم'),
        ('medium', 'متوسط'),
        ('high', 'بالا'),
        ('urgent', 'فوری'),
    ]

    STATUS_CHOICES = [
        ('new', 'جدید'),
        ('in_review', 'در حال بررسی'),
        ('contacted', 'تماس گرفته شده'),
        ('quoted', 'پیش ‌فاکتور ارسال شده'),
        ('closed', 'بسته شده'),
    ]

    full_name = models.CharField(max_length=100, verbose_name='نام کامل')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=15, verbose_name='تلفن')
    company = models.CharField(max_length=100, blank=True, verbose_name='شرکت')
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES, verbose_name='نوع خدمات')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium', verbose_name='اولویت')
    title = models.CharField(max_length=200, blank=True, verbose_name='عنوان پروژه')
    description = models.TextField(verbose_name='توضیحات پروژه')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')

    def __str__(self):
        return f'{self.full_name} - {self.service_type}'

    class Meta:
        verbose_name = 'درخواست مشتری'
        verbose_name_plural = 'درخواست‌های مشتریان'
        ordering = ['-created_at']