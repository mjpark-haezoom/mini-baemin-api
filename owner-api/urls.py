# owner-api/urls.py
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("v1/auth/", include("accounts.urls_owner")),
    # 사장님용 엔드포인트 분리 (가게 관리, 메뉴 수정 등)
    path("v1/owner/", include("stores.owner_urls")),
    #  API 문서 관련 URL
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
