from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Пользовательская модель User"""

    pass


class Profile(models.Model):
    """Модель профиля пользователя с общими полями"""

    USER_TYPE = (
        (1, "Администратор"),
        (2, "Работник"),
        (3, "Руководитель"),
    )

    GENDER = [
        ("M", "Мужской"),
        ("F", "Женский"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    user_type = models.CharField(
        default=2,
        choices=USER_TYPE,
        max_length=1,
        verbose_name="Тип пользователя",
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        verbose_name="Пол",
    )

    address = models.TextField(
        blank=True,
        verbose_name="Адрес",
    )

    # phone = models.CharField(max_length=20, blank=True, verbose_name="Номер телефона")
    phone = PhoneNumberField(
        blank=True,
        unique=True,
        verbose_name="Номер телефона",
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата рождения",
    )

    date_joined = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата принятия на работу",
    )

    skills = models.TextField(
        blank=True,
        verbose_name="Навыки и компетенции",
    )

    bio = models.TextField(
        blank=True,
        verbose_name="Краткая биография",
    )

    social_links = models.URLField(
        null=True,
        blank=True,
        verbose_name="Ссылка на социальные сети",
    )

    emergency_contact_name = models.CharField(
        blank=True,
        max_length=100,
        verbose_name="Имя контактного лица для экстренных случаев",
    )
    emergency_contact_phone = PhoneNumberField(
        blank=True,
        max_length=20,
        verbose_name="Телефон для экстренных случаев",
    )

    contract_type = models.CharField(
        blank=True,
        max_length=50,
        verbose_name="Тип трудового договора (постоянный, временный и т. д.)",
    )

    profile_picture = models.ImageField(
        blank=True,
        verbose_name="Фотография профиля",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего обновления",
        help_text="",
    )

    def __str__(self) -> str:
        return f"{self.user.last_name} {self.user.first_name}"

    class Meta:
        verbose_name = "профиль"
        verbose_name_plural = "профили"


class Employee(models.Model):
    pass


class Admin(models.Model):
    # admin = models.OneToOneField(Profile, on_delete=models.CASCADE)
    pass


class Manager(models.Model):
    pass
