# owner-api/urls.py
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # 사장님용 관리자 페이지
    path("admin/", admin.site.urls),

    # 사장님용 엔드포인트 분리 (가게 관리, 메뉴 수정 등)
    path("api/v1/owner/", include("stores.owner_urls")),

    #  API 문서 관련 URL
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), \
            name="swagger-ui"),
]


