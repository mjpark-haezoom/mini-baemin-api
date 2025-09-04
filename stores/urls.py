# stores/urls.py

from django.urls import path

from .consumer_views import MenuListView, StoreListView

urlpatterns = [
    # 상점 목록
    path("", StoreListView.as_view(), name="store-list"),
    # 메뉴 조회
    path("<int:store_id>/menus/", MenuListView.as_view(), name="menu-list"),
]
