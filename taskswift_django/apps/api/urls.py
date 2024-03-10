from django.urls import include, path

urlpatterns = [
    path("tasks/", include("api.tasks.urls")),
    path("users/", include("api.users.urls")),
]
