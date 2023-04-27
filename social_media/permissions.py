from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrIfAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user and (
                request.user.is_staff or request.user.is_authenticated
        )
