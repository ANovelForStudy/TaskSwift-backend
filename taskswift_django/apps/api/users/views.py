# from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsManager
from users.models import CustomUser, UserType

from .serializers import CustomUserSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = CustomUser.objects.filter(user_type="1", is_staff=False, is_superuser=False)
    serializer_class = CustomUserSerializer
    permission_classes = [IsManager]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.user_type == UserType.EMPLOYEE:
            return Response(
                {"detail": "Сотрудникам не разрешено удалять аккаунты пользователей."},
                status=status.HTTP_403_FORBIDDEN,
            )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
