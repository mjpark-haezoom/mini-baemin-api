# admin-api/middleware.py
import re
from django.http import HttpResponseForbidden

_ADMIN_PATH_RE = re.compile(r"^/admin(?:/|$)")

def _is_developer(u):
    # Admin 접근은 항상 is_staff 전제
    if not (u and u.is_authenticated and u.is_staff):
        return False
    in_dev_group = hasattr(u, "groups") and u.groups.filter(name="developer").exists()
    is_admin_type = getattr(u, "user_type", None) == "admin"  # 레거시 필드 사용 시
    return bool(u.is_superuser or in_dev_group or is_admin_type)

class AdminOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if _ADMIN_PATH_RE.match(request.path):
            u = request.user
            if not _is_developer(u):
                return HttpResponseForbidden("Admin only")
        return self.get_response(request)