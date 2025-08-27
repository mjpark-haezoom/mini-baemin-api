# consumer-api/urls.py
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("api/v1/stores/", include("stores.urls")),      # 소비자용 공개 스토어 URL

    # API 문서 관련 URL
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), \
            name="swagger-ui"),
]


