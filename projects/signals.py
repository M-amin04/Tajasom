from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Project

@receiver(pre_save, sender=Project)
def create_project_slug(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.title, allow_unicode=True)
        slug = base_slug
        counter = 1
        while Project.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        instance.slug = slug