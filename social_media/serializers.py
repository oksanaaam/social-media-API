from rest_framework import serializers

from social_media.models import Post, Like, Comment, Profile
from user.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    is_staff = serializers.CharField(source="user.is_staff", read_only=True)
    user = serializers.CharField(source="user.id", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    followers = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    posts = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = ("id", "user", "email", "bio", "avatar", "followers", "posts", "is_staff")


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
