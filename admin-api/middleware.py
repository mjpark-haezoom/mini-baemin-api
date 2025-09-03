from django.http import HttpResponseForbidden

def _is_developer(u):
    return (
        u.is_superuser
        or (u.is_staff and (
            getattr(u, "user_type", None) == "admin" or
            (hasattr(u, "groups") and u.groups.filter(name="developer").exists())
        ))
    )

class AdminOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if request.path.startswith("/admin/"):
            u = request.user
            if not (u.is_authenticated and _is_developer(u)):
                return HttpResponseForbidden("Admin only")
        return self.get_response(request)
