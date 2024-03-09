from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS + ('POST', ) or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )
