from django.urls import path

from api.tasks import views

task_urls = [
    # Получение всех записей о задачах и создание новой задачи
    path(
        "",
        views.TaskViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="task_list",
    ),
    # Получение, удаление, изменение записи о конкретной задаче
    path(
        "<int:pk>/",
        views.TaskViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="task_detail",
    ),
    path(
        "<int:pk>/toggle_completion/",
        views.TaskViewSet.as_view(
            {
                "post": "toggle_completion",
            }
        ),
        name="toggle_task_completion",
    ),
    path(
        "assigned-to-me/",
        views.TaskViewSet.as_view(
            {
                "get": "assigned_to_me",
            }
        ),
        name="assigned_to_me",
    ),
]

task_category_urls = [
    # Получение всех записей о категориях задач и создание новой категории
    path(
        "categories/",
        views.TaskCategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="task_category_list",
    ),
    # Получение, удаление, изменение записи о конкретной категории задач
    path(
        "categories/<int:pk>/",
        views.TaskCategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="task_category_detail",
    ),
]

urlpatterns = task_urls + task_category_urls
