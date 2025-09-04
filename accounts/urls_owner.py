# accounts/urls_owner.py

from django.urls import path

from .views_owner import OwnerLoginView, OwnerRegisterView, OwnerView

urlpatterns = [
    path("signup/", OwnerRegisterView.as_view(), name="owner-signup"),
    path("login/", OwnerLoginView.as_view(), name="owner-login"),
    path("me/", OwnerView.as_view(), name="owner-me"),
]
