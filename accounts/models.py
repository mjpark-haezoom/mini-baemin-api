# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class ConsumerUser(AbstractUser):
    """
    소비자 사용자 모델 - 이메일 기반 인증
    """
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        verbose_name="Email Address"
    )

    # groups 필드에 고유한 related_name을 추가
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='consumer_user_groups_set',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        verbose_name='groups',
    )
    # user_permissions 필드에 고유한 related_name을 추가
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='consumer_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = 'accounts_consumeruser'
        verbose_name = "Consumer User"
        verbose_name_plural = "Consumer Users"

    def __str__(self):
        return self.email


class OwnerUser(AbstractUser):
    """
    점주 사용자 모델 - 전화번호 기반 인증
    """
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        blank=False,
        null=False,
        verbose_name="Phone Number"
    )
    business_license = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Business License Number"
    )
    store_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Store Name"
    )

    # groups 필드에 고유한 related_name을 추가
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='owner_user_groups_set',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        verbose_name='groups',
    )
    # user_permissions 필드에 고유한 related_name을 추가
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='owner_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = 'accounts_owneruser'
        verbose_name = "Owner User"
        verbose_name_plural = "Owner Users"

    def __str__(self):
        return self.phone_number


class OperatorUser(AbstractUser):
    """
    운영자 사용자 모델 - 직원ID 기반 인증
    """
    employee_id = models.CharField(
        max_length=20,
        unique=True,
        blank=False,
        null=False,
        verbose_name="Employee ID"
    )
    department = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Department"
    )
    position = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Position"
    )

    # groups 필드에 고유한 related_name을 추가
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='operator_user_groups_set',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        verbose_name='groups',
    )
    # user_permissions 필드에 고유한 related_name을 추가
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='operator_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = "employee_id"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = 'accounts_operatoruser'
        verbose_name = "Operator User"
        verbose_name_plural = "Operator Users"

    def __str__(self):
        return self.employee_id


# 기존 User 모델은 호환성을 위해 유지 (deprecated)
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

    # groups 필드에 고유한 related_name을 추가
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups_set',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        verbose_name='groups',
    )
    # user_permissions 필드에 고유한 related_name을 추가
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = 'accounts_user'
        verbose_name = "Legacy User"
        verbose_name_plural = "Legacy Users"

    def __str__(self):
        return self.username