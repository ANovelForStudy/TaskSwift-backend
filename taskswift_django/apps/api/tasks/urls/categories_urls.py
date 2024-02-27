from api.tasks import views
from django.urls import path

urlpatterns = [
    # Получение всех записей о категориях задач и создание новой категории
    path("", views.TaskCategoryListCreateAPIView.as_view(), name="task_category_list"),
    # Получение, удаление, изменение записи о конкретной категории задач
    path("<int:pk>/", views.TaskCategoryRetrieveUpdateDestroyAPIView.as_view(), name="task_category_detail"),
]
