# consumer-api/urls.py
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("v1/auth/", include("accounts.urls_consumer")),
    path("v1/stores/", include("stores.urls_consumer")),
    # API 문서 관련 URL
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
