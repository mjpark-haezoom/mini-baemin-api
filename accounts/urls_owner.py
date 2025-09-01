# accounts/urls_owner.py

from django.urls import path

from .views_owner import OwnerLoginView, OwnerView


urlpatterns = [
    path("login/", OwnerLoginView.as_view(), name="owner-login"),
    path("me/", OwnerView.as_view(), name="owner-me"),
]


