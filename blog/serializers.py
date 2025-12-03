from rest_framework import serializers
from .models import Blog, Comment, Category


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id', 'blog', 'author_name', 'author_email', 'content', 'rating', 'is_approved', 'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'is_approved', 'blog']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False
    )

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'content', 'cover_image',
            'category', 'category_id', 'author', 'view_count', 'created_at', 'updated_at',
            'is_published', 'is_featured', 'published_at',
            'comments', 'comments_count'
        ]
        read_only_fields = ['id', 'slug', 'view_count', 'created_at', 'updated_at']

    def get_comments_count(self, obj):
        return obj.comments.count()
