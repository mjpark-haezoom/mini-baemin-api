# accounts/urls.py

from django.urls import include, path

from .views import LoginView, UserRegisterView

urlpatterns = [
    path("signup/", UserRegisterView.as_view(), name="user-signup"),
    path("login/", LoginView.as_view(), name="user-login"),
    path("api/v1/stores/", include("stores.urls")),
]
