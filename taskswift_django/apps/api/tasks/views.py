from rest_framework.viewsets import ModelViewSet
from tasks.models import Task, TaskCategory

from .serializers import TaskCategorySerializer, TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCategoryViewSet(ModelViewSet):
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializer
