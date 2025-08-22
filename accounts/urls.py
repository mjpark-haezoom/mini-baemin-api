# accounts/urls.py

from django.urls import path

from .views import LoginView, UserRegisterView

urlpatterns = [
    path("signup/", UserRegisterView.as_view(), name="user-signup"),
    path("login/", LoginView.as_view(), name="user-login")
]
