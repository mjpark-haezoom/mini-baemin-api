from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 스키마 (JSON)
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path(
        "api/docs/", SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger-ui"
    ),
    # 앱 URL
    path("api/v1/", include("accounts.urls"))
]
