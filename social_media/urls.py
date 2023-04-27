from django.urls import path, include
from rest_framework import routers

from social_media.views import PostViewSet, LikeViewSet, CommentViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register("profile", ProfileViewSet)
router.register("posts", PostViewSet)
router.register("likes", LikeViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "social_media"