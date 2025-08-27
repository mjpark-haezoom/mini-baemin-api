# accounts/permissions.py

from rest_framework.permissions import BasePermission
from django.conf import settings

class AllowUserTypes(BasePermission):
    """
    Custom permission to only allow access to specific user types defined in settings.
    settings.ALLOWED_USER_TYPES = ["consumer"]  # For consumer-api
    settings.ALLOWED_USER_TYPES = ["owner"]     # For owner-api
    """
    def has_permission(self, request, view):
        # Allow if the user is not authenticated (for public endpoints)
        # or if the user type is in the allowed list.
        if not request.user or not request.user.is_authenticated:
            return True

        allowed_types = getattr(settings, "ALLOWED_USER_TYPES", [])
        return request.user.user_type in allowed_types