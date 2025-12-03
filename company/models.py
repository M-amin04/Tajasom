from django.db import models


class CompanyHistory(models.Model):
    year = models.CharField(max_length=10, verbose_name='سال')
    title = models.CharField(max_length=200, verbose_name='عنوان رویداد')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='history/', blank=True, null=True, verbose_name='تصویر')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.year} - {self.title}'

    class Meta:
        verbose_name = 'تاریخچه'
        verbose_name_plural = 'تاریخچه'
        ordering = ['order', 'year']


class TeamMember(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    position = models.CharField(max_length=100, verbose_name='سمت')
    bio = models.TextField(blank=True, verbose_name='بیوگرافی')
    image = models.ImageField(upload_to='team/', verbose_name='تصویر')
    email = models.EmailField(blank=True, verbose_name='ایمیل')
    phone = models.CharField(max_length=20, blank=True, verbose_name='تلفن')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        verbose_name = 'عضو تیم'
        verbose_name_plural = 'اعضای تیم'
        ordering = ['order', 'created_at']


class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام شرکت')
    description = models.TextField(verbose_name='توضیحات شرکت')
    mission = models.TextField(blank=True, verbose_name='ماموریت')
    vision = models.TextField(blank=True, verbose_name='چشم‌انداز')
    values = models.TextField(blank=True, verbose_name='ارزش‌ها')
    years_experience = models.PositiveIntegerField(default=0, verbose_name='سال تجربه')
    completed_projects = models.PositiveIntegerField(default=0, verbose_name='پروژه‌های تکمیل شده')
    happy_clients = models.PositiveIntegerField(default=0, verbose_name='مشتریان راضی')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اطلاعات شرکت'
        verbose_name_plural = 'اطلاعات شرکت'


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام شرکت')
    logo = models.ImageField(upload_to='clients/', verbose_name='لوگو')
    website = models.URLField(blank=True, verbose_name='وبسایت')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'
        ordering = ['order']


class CompanyContact(models.Model):
    address = models.TextField(verbose_name='آدرس')
    phone = models.CharField(max_length=20, verbose_name='تلفن')
    email = models.EmailField(verbose_name='ایمیل')
    working_hours = models.TextField(verbose_name='ساعات کاری')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "اطلاعات تماس شرکت"

    class Meta:
        verbose_name = 'اطلاعات تماس'
        verbose_name_plural = 'اطلاعات تماس'