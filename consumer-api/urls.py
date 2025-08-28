# consumer-api/urls.py
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # 소비자용 stores 앱 URL
    path("stores/", include("stores.urls")),

    # API 문서 관련 URL
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url="/api/consumer/schema/"), \
            name="swagger-ui"),

]


