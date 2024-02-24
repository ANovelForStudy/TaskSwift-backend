from django.db import models


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = "L", "Низкий"
        MEDIUM = "M", "Средний"
        HIGH = "H", "Высокий"
        UNDEFINED = "U", "Не определён"

    title = models.CharField(max_length=255)
    description = models.TextField()

    # category = models.CharField(null=True, blank=True)

    # assigned_to = models.ForeignKey()

    # created_at = models.DateTimeField(auto_now_add=True)
    # deadline = models.DateTimeField(null=True, blank=True)

    priority = models.CharField(max_length=2, choices=Priority.choices, default=Priority.UNDEFINED)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "задачи"
