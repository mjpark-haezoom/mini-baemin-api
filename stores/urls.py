# stores/urls.py

from django.urls import path

from .views import MenuListView, StoreListView

urlpatterns = [
    # GET /api/v1/stores
    path("", StoreListView.as_view(), name="store-list"),

    # GET /api/v1/stores/{store_id}/menus
    path("<int:store_id>/menus", MenuListView.as_view(), name="menu-list"),
]
