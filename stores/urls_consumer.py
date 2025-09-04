# stores/urls_consumer.py

from django.urls import path

from .consumer_views import MenuListView, StoreListView

urlpatterns = [
    path("", StoreListView.as_view(), name="consumer-store-list"),
    path("<int:store_id>/menus/", MenuListView.as_view(), name="consumer-menu-list"),
]
