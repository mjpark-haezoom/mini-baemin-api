# backend/urls.py

from django.contrib import admin
from django.urls import include, path

# drf-spectacular 관련 import
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("accounts.urls")),
    path("api/v1/stores/", include("stores.urls")),

    # OpenAPI 스키마 (JSON)
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path(
        "api/docs/", SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger-ui"
    ),
]
