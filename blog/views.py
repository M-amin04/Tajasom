from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.filter(is_published=True).prefetch_related('comments')
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category_id', 'is_featured']
    search_fields = ['title', 'content', 'author']
    ordering_fields = ['created_at', 'published_at', 'view_count']
    ordering = ['-published_at']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        ser = self.get_serializer(instance)
        return Response(ser.data)

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        blog = self.get_object()
        ser = CommentSerializer(data=request.data)
        if ser.is_valid():
            ser.save(blog=blog)
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def related_posts(self, request, pk=None):
        blog = self.get_object()
        related_posts = Blog.objects.filter(
            category_id=blog.category_id,
            is_published=True
        ).exclude(id=blog.id)[:4]
        ser = BlogSerializer(related_posts, many=True)
        return Response(ser.data)

    @action(detail=False, methods=['get'], url_path='slug/(?P<slug>[^/.]+)')
    def get_by_slug(self, request, slug=None):
        try:
            blog = Blog.objects.get(slug=slug, is_published=True)
            blog.view_count += 1
            blog.save()
            serializer = self.get_serializer(blog)
            return Response(serializer.data)
        except Blog.DoesNotExist:
            return Response({'error': 'مقاله یافت نشد'}, status=status.HTTP_404_NOT_FOUND)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_approved=True)
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'head', 'options', 'post']

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        comment = self.get_object()
        comment.is_approved = True
        comment.save()
        return Response({'status': 'comment approved'})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        comment = self.get_object()
        comment.is_approved = False
        comment.save()
        return Response({'status': 'comment rejected'})
