# stores/owner_urls.py

from django.urls import path

from .owner_views import OwnerStoreCreateView

urlpatterns = [
    # 사장님 전용 기능
    # 가게 생성 API
    path("stores/", OwnerStoreCreateView.as_view(), name="store-create"),
]
