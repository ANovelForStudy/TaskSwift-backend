from api.tasks import views
from django.urls import path

urlpatterns = [
    # Получение всех записей о задачах и создание новой задачи
    path("", views.TaskListCreateAPIView.as_view(), name="task_list"),
    # Получение, удаление, изменение записи о конкретной задаче
    path("<int:pk>/", views.TaskRetrieveUpdateDestroyAPIView.as_view(), name="task_detail"),
]
