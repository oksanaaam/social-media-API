
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from social_media.models import Post, Like, Comment
from social_media.permissions import IsAdminOrIfAuthenticated
from social_media.serializers import PostSerializer, LikeSerializer, CommentSerializer, PostListSerializer, \
    PostDetailSerializer, PostImageSerializer
from user.serializers import UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrIfAuthenticated,)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
