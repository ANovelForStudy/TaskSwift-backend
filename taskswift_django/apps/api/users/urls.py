from django.urls import path

from api.users import views

urlpatterns = [
    # path(
    #     "employees/",
    #     views.EmployeeList.as_view(),
    #     name="employees-list",
    # ),
    path(
        "employees/",
        views.TaskViewSet.as_view(
            {
                "get": "list",
                "post": "create",
                "delete": "destroy",
            }
        ),
        name="employees-list",
    ),
]
