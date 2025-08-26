# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/v1/stores/", include("stores.urls")),      # 공개 스토어 조회
    path("api/v1/owner/", include("stores.owner_urls")), # 오너용 엔드포인트 분리

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]


