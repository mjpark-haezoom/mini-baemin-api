# consumer-api/urls.py
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("v1/auth/", include("accounts.urls")),
    path("v1/stores/", include("stores.urls")),

    # API 문서 관련 URL
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url="/api/consumer/schema/"), \
            name="swagger-ui"),

]


