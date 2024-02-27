from django.urls import include, path

from .tasks.urls import categories_urls, tasks_urls

urlpatterns = [
    path("tasks/", include(tasks_urls)),
    path("task-categories/", include(categories_urls)),
]
