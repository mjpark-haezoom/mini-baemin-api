# accounts/permissions.py

from rest_framework.permissions import BasePermission
from django.conf import settings

class AllowUserTypes(BasePermission):
    """
    Custom permission to only allow access to specific user types defined in settings.
    settings.ALLOWED_USER_TYPES = ["consumer"]  # For consumer-api
    settings.ALLOWED_USER_TYPES = ["owner"]     # For owner-api
    settings.ALLOWED_USER_TYPES = ["operator"]  # For backoffice-api
    """
    def has_permission(self, request, view):
        # Allow if the user is not authenticated (for public endpoints)
        # or if the user type is in the allowed list.
        if not request.user or not request.user.is_authenticated:
            return False

        # allowed user type list from settings.
        allowed_types = getattr(settings, "ALLOWED_USER_TYPES", [])

        # Determine user type based on the user model class
        user_type = self._get_user_type(request.user)

        # if user.user_type is in list -> True or False
        return user_type in allowed_types

    def _get_user_type(self, user):
        """
        Determine user type based on the user model class
        """
        from .models import ConsumerUser, OwnerUser, OperatorUser

        if isinstance(user, ConsumerUser):
            return "consumer"
        elif isinstance(user, OwnerUser):
            return "owner"
        elif isinstance(user, OperatorUser):
            return "operator"
        else:
            # Fallback for legacy User model
            return getattr(user, 'user_type', None)