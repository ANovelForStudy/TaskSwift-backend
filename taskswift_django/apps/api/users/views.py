# from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsManager
from users.models import CustomUser

from .serializers import CustomUserSerializer

# class EmployeeList(generics.ListAPIView):
#     queryset = CustomUser.objects.filter(user_type="1")
#     serializer_class = CustomUserSerializer
#     permission_classes = [IsManager]


class TaskViewSet(ModelViewSet):
    queryset = CustomUser.objects.filter(user_type="1", is_staff=False, is_superuser=False)
    serializer_class = CustomUserSerializer
    permission_classes = [IsManager]
