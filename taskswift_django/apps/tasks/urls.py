from django.urls import path

from . import views

urlpatterns = [
    # ЗАДАЧИ
    # Получение всех записей о задачах и создание новой задачи
    path(
        "",
        views.TaskListCreateAPIView.as_view(),
    ),
    # Получение, удаление, изменение записи о конкретной задаче
    path(
        "detail/<int:pk>/",
        views.TaskRetrieveUpdateDestroyAPIView.as_view(),
    ),
    # КАТЕГОРИИ ЗАДАЧ
    # Получение всех записей о категориях задач и создание новой категории
    path(
        "categories/",
        views.TaskCategoryListCreateAPIView.as_view(),
    ),
    # Получение, удаление, изменение записи о конкретной категории задач
    path(
        "categories/detail/<int:pk>/",
        views.TaskCategoryRetrieveUpdateDestroyAPIView.as_view(),
    ),
]
