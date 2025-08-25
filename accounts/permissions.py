# accounts/permissions.py

from rest_framework import permissions

class IsConsumer(permissions.BasePermission): # 일반 소비자
    """Permission class to allow access only to users with the 'consumer' type."""
    def has_permission(self, request, view):
        # Allow access if the user is authenticated and has the 'consumer' user_type
        return request.user.is_authenticated and request.user.user_type == 'consumer'

class IsOwner(permissions.BasePermission): # 점주 (사장님)
    """Permission class to allow access only to users with the 'owner' type."""
    def has_permission(self, request, view):
        # Allow access if the user is authenticated and has the 'owner' user_type
        return request.user.is_authenticated and request.user.user_type == 'owner'

class IsOperator(permissions.BasePermission): # 배민 운영자
    """Permission class to allow access only to users with the 'operator' type."""
    def has_permission(self, request, view):
        # Allow access if the user is authenticated and has the 'operator' user_type
        return request.user.is_authenticated and request.user.user_type == 'operator'


