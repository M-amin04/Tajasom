from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from blog.models import Blog


@receiver(pre_save, sender=Blog)
def create_blog_slug(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.title, allow_unicode=True)
        slug = base_slug
        counter = 1
        while Blog.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        instance.slug = slug