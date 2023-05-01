from rest_framework import serializers

from social_media.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "content", "created_at", "author")
        read_only_fields = ("id", "owner")


class PostListSerializer(PostSerializer):

    class Meta:
        model = Post
        fields = ("id", "content", "image", "created_at", "author")
        read_only_fields = ("id", "owner")
