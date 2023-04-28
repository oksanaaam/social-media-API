from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import Profile
from user.serializers import UserSerializer, ProfileListSerializer, ProfileDetailSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        email = self.request.query_params.get("email")
        queryset = self.queryset
        if email:
            queryset = queryset.filter(user__email__icontains=email)
        return queryset.select_related("user").prefetch_related("followers").distinct()

    def get_serializer_class(self):
        if self.action == "list":
            return self.serializer_class
        return ProfileDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(
        methods=["GET"],
        detail=True,
        url_path="follow",
    )
    def follow_unfollow(self, request: Request, pk: int = None) -> Response:
        user = get_user_model().objects.get(id=request.user.id)
        following = get_user_model().objects.get(id=pk)
        if user != following:
            if user in following.profile.followers.all():
                following.profile.followers.remove(user.id)
            else:
                following.profile.followers.add(user.id)

            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "username",
                type=str,
                description="Filter by username that contains specified symbol(s), "
                            "case insensitive (ex. ?username=oo)",
            ),
            OpenApiParameter(
                "bio",
                type=str,
                description="Filter by bio that contains specified symbol(s), "
                            "case insensitive (ex. ?bio=oo)",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
