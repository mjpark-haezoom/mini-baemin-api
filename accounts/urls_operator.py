# accounts/urls_operator.py

from django.urls import path

from .views_operator import OperatorLoginView, OperatorView


urlpatterns = [
    path("login/", OperatorLoginView.as_view(), name="operator-login"),
    path("me/", OperatorView.as_view(), name="operator-me"),
]

