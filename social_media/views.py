from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets

from social_media.models import Post
from social_media.permissions import IsAuthenticatedOrReadOnly
from social_media.serializers import PostSerializer, PostListSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    @staticmethod
    def _params_to_ints(qs):
        """Converts a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        following_list = self.request.user.profile.following.all()

        queryset = self.queryset.filter(
            user__in=list(following_list) + [self.request.user.id]
        )

        content = self.request.query_params.get("content")

        if content:
            queryset = queryset.filter(content__icontains=content)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PostListSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "content",
                type=str,
                description="Filter by case insensitive content (ex. ?content=sport)",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
