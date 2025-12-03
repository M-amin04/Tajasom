from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', BlogViewSet, basename='blog-posts')
router.register(r'comments', CommentViewSet, basename='blog-comments')

urlpatterns = [
    path('', include(router.urls)),
]