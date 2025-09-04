# admin-api/permissions.py

from rest_framework.permissions import BasePermission


def is_developer(u):
    return u.is_authenticated and (
        u.is_superuser
        or (
            u.is_staff
            and (
                getattr(u, "user_type", None) == "admin"
                or (hasattr(u, "groups") and u.groups.filter(name="developer").exists())
            )
        )
    )


class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        return is_developer(request.user)
