from rest_framework import serializers
from tasks.models import Task, TaskCategory


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "priority",
            "color",
            "category",
            "assigned_to",
            "deadline",
            "created_at",
            "updated_at",
        ]


class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = "__all__"
