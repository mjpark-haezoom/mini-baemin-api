# accounts/permissions.py

from rest_framework import permissions


class IsUserType(permissions.BasePermission):
    def has_permission(self, request, view):
        # Checks if the user is authenticated and \
        # if their user_type matches the one specified
        # during class instantiation.
        required_user_type = getattr(view, "user_type", None)
        if not required_user_type:
            return False  # Or handle as an error
        return request.user.is_authenticated and \
               request.user.user_type == required_user_type