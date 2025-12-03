from django.contrib import admin
from .models import Blog, Comment, Category

admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_published', 'is_featured', 'view_count', 'created_at']
    list_filter = ['category', 'is_published', 'is_featured']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'author_name', 'content_short', 'rating', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'rating', 'blog']
    search_fields = ['author_name', 'content', 'blog__title']
    actions = ['approve_comments', 'reject_comments']

    def content_short(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    content_short.short_description = 'متن نظر'

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)

    approve_comments.short_description = 'تأیید نظرات انتخاب شده'

    def reject_comments(self, request, queryset):
        queryset.update(is_approved=False)

    reject_comments.short_description = 'رد نظرات انتخاب شده'