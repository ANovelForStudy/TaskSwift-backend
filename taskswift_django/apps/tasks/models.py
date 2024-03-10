from colorfield.fields import ColorField
from django.db import models

from users.models import CustomUser, Employee


class TaskCategory(models.Model):
    """Модель категории для задач"""

    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
    )

    description = models.TextField(
        verbose_name="Описание категории",
        blank=True,
    )

    color = ColorField(
        default="#FFFFFF",
        verbose_name="Цвет для категории",
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
        return self.name

    class Meta:
        verbose_name = "категория задач"
        verbose_name_plural = "категории задач"


class Task(models.Model):
    """Модель задачи"""

    class Priority(models.TextChoices):
        LOW = "L", "Низкий"
        MEDIUM = "M", "Средний"
        HIGH = "H", "Высокий"
        UNDEFINED = "U", "Не определён"

    title = models.CharField(
        max_length=255,
        verbose_name="Название задачи",
    )

    description = models.TextField(
        verbose_name="Описание задачи",
        blank=True,
    )

    priority = models.CharField(
        max_length=2,
        choices=Priority.choices,
        default=Priority.UNDEFINED,
        verbose_name="Приоритет задачи",
    )

    color = ColorField(
        default="#FFFFFF",
        verbose_name="Цвет для задачи",
    )

    category = models.ForeignKey(
        TaskCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория задачи",
    )

    assigned_to = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Исполнитель задачи",
        help_text="Кому задача назначена для выполнения",
    )

    is_completed = models.BooleanField(
        default=False,
        verbose_name="Задача выполнена",
        help_text="Статус выполнения задачи",
    )

    deadline = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дедлайн (крайний срок)",
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
        return self.title

    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "задачи"
