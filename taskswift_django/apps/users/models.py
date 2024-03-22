from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(UserManager):
    """Пользовательский UserManager для кастомизированной модели CustomUser"""

    # use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Проверки на то, что необходимые поля для суперпользователя существуют
        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]

        return self._create_user(email, password, **extra_fields)


class UserType(models.TextChoices):
    EMPLOYEE = "1", "Работник"
    MANAGER = "2", "Руководитель"
    ADMIN = "3", "Администратор"


class CustomUser(AbstractUser):
    """Пользовательская модель User без поля username"""

    GENDER = [
        ("M", "Мужской"),
        ("F", "Женский"),
    ]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # Назначение кастомизированного UserManager
    objects = CustomUserManager()

    # Отказ от использования username в пользу использования email
    username = None

    first_name = models.CharField(
        max_length=150,
        verbose_name="Имя",
    )

    middle_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Отчество",
    )

    last_name = models.CharField(
        max_length=150,
        verbose_name="Фамилия",
    )

    email = models.EmailField(unique=True)

    user_type = models.CharField(
        default="1",
        choices=UserType.choices,
        max_length=1,
        verbose_name="Тип пользователя",
    )

    gender = models.CharField(
        blank=True,
        max_length=1,
        choices=GENDER,
        verbose_name="Пол",
    )

    address = models.TextField(
        blank=True,
        verbose_name="Адрес",
    )

    phone = PhoneNumberField(
        blank=True,
        null=True,
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
        verbose_name="Дата устройства на работу",
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

    profile_picture = models.ImageField(
        null=True,
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
    )

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"


class Admin(models.Model):
    """Модель администратора"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Employee(models.Model):
    """Модель работника"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    contract_type = models.CharField(
        blank=True,
        max_length=50,
        verbose_name="Тип трудового договора (постоянный, временный и т. д.)",
    )

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"

    def __str__(self) -> str:
        return f"{self.user.last_name}, {self.user.first_name}"


class Manager(models.Model):
    """Модель руководителя"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "руководитель"
        verbose_name_plural = "руководители"

    def __str__(self) -> str:
        return f"{self.user.last_name}, {self.user.first_name}"
