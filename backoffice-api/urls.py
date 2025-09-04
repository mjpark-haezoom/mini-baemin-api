# backoffice-api/urls.py
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # 관리자 페이지
    path("admin/", admin.site.urls),
    path("v1/auth/", include("accounts.urls_operator")),
    # path("v1/org/", include("accounts.urls_org")),
    # API 문서 관련 URL
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
