from rest_framework import serializers

from blog.models import Post, PostTag, Tag


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Post


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Tag
