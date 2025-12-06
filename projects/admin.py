from django.contrib import admin
from .models import Project, ProjectImage, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'is_featured', 'is_active', 'created_at']
    list_filter = ['category', 'status', 'is_featured', 'is_active']
    search_fields = ['title', 'description']
    list_select_related = ['category']


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'title', 'order', 'is_main']