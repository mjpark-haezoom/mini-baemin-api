# accounts/urls_consumer.py

from django.urls import path

from .views_consumer import ConsumerView, LoginView, UserRegisterView


urlpatterns = [
    path("signup/", UserRegisterView.as_view(), name="consumer-signup"),
    path("login/", LoginView.as_view(), name="consumer-login"),
    path("me/", ConsumerView.as_view(), name="consumer-me"),
]


