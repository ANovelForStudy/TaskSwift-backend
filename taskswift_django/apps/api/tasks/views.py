from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tasks.models import Task, TaskCategory

from .serializers import TaskCategorySerializer, TaskSerializer


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCategoryListCreateAPIView(ListCreateAPIView):
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializer


class TaskCategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializer
