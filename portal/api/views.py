from django.shortcuts import render
from rest_framework import viewsets, status
from drf_spectacular.utils import extend_schema

from blog.models import Post, PostTag, Tag
from api.serializers import (
    PostSerializer,
    TagSerializer
)
from api.pagination import CustomPagination


@extend_schema(tags=["Post"])
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination


@extend_schema(tags=["Tag"])
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """Tag."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = CustomPagination
