# backend/urls.py

from django.contrib import admin
from django.urls import include, path

# drf-spectacular 관련 import
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("accounts.urls")),

    # Swagger/Open API 관련 URL
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui"
    ),
]
