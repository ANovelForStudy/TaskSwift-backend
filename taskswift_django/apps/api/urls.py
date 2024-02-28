from django.urls import include, path

from .tasks import tasks_urls

urlpatterns = [
    path("tasks/", include(tasks_urls)),
]
