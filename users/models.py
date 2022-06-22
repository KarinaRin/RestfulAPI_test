from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password):
        return self._create_user(email, password)

    def create_superuser(self, email, password):
        return self._create_user(email, password, is_staff=True, is_superuser=True)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    roles = (
        ('Subscriber', 'Подписчик'),
        ('Author', 'Автор'),
    )
    user_role = models.CharField(verbose_name='Роль пользователя', choices=roles, default='Subscriber', max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
