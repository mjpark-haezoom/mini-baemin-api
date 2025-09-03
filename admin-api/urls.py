# backoffice-api/urls.py
from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

def health(_): return JsonResponse({"status": "ok"})

urlpatterns = [
    # 관리자 페이지
    path("admin/", admin.site.urls),
    path("health", health)
]


