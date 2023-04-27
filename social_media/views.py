
from rest_framework import viewsets

from social_media.models import Post, Like, Comment, Profile
from social_media.permissions import IsAdminOrIfAuthenticated
from social_media.serializers import PostSerializer, LikeSerializer, CommentSerializer, PostListSerializer, \
    PostDetailSerializer, PostImageSerializer, ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminOrIfAuthenticated,)


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
