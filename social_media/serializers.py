from rest_framework import serializers

from social_media.models import Post, Like, Comment
from user.serializers import UserSerializer


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = ("id", "user", "created_at")


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ("id", "user", "content", "created_at")


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "content", "created_at", "author")


class PostListSerializer(PostSerializer):

    class Meta:
        model = Post
        fields = ("id", "content", "image", "created_at", "author", "count_comments", "count_likes")


class PostDetailSerializer(PostSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    liked_by = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "content",
            "image",
            "created_at",
            "author",
            "comments",
            "count_comments",
            "count_likes",
            "liked_by"
        )


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "image")
