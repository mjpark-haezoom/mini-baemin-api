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
        verbose_name="사용자 유형"
    )
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        verbose_name="전화번호"
    )

    def __str__(self):
        return self.username
