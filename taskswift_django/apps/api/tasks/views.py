from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsManager
from tasks.models import Task, TaskCategory
from users.models import UserType

from .serializers import TaskCategorySerializer, TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # @action(detail=True, methods=["post"])
    # def mark_task_completed(self, request, pk=None):
    #     task = self.get_object()
    #     task.is_completed = True
    #     task.save()
    #     serializer = TaskSerializer(task)
    #     return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.user_type == UserType.EMPLOYEE:
            return Response(
                {"detail": "Сотрудникам не разрешено редактировать задачи."}, status=status.HTTP_403_FORBIDDEN
            )
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.user_type == UserType.EMPLOYEE:
            return Response({"detail": "Сотрудникам не разрешено удалять задачи."}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        if request.user.user_type != UserType.MANAGER:
            return Response(
                {"detail": "Вы не имеете прав для просмотра всех задач."}, status=status.HTTP_403_FORBIDDEN
            )
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=["post"])
    def toggle_completion(self, request, pk=None):
        task = self.get_object()
        task.is_completed = not task.is_completed
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def assigned_to_me(self, request):
        assigned_to = request.user.id
        tasks = Task.objects.filter(assigned_to=assigned_to)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskCategoryViewSet(ModelViewSet):
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializer
    # permission_classes = [IsManager]
