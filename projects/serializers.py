from rest_framework import serializers
from .models import Project, ProjectImage, Category


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'title', 'description', 'order', 'is_main']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Project
        fields = ['id', 'title', 'slug', 'description', 'category', 'status',
                  'image', 'client_name', 'project_date', 'location', 'duration', 'scale', 'materials',
                  'special_features', 'order', 'is_featured', 'is_active', 'created_at', 'images'
                  ]
        read_only_fields = ['id', 'slug', 'created_at']
