from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ("consumer", "consumer"),
        ("owner", "owner"),
        ("operator", "operator"),
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default="consumer",
        verbose_name="User Type"
    )
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Phone Number"
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        verbose_name="Email Address"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
