from django.urls import path

from api.users import views

urlpatterns = [
    # Получение списка сотрудников, а также создание записи сотрудника
    path(
        "employees/",
        views.EmployeeViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="employees_list",
    ),
    # Получение, удаление, изменение записи о конкретном сотруднике
    path(
        "employees/<int:pk>/",
        views.EmployeeViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="employee_detail",
    ),
]
