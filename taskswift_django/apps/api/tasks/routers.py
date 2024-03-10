from rest_framework import routers

from .views import TaskCategoryViewSet, TaskViewSet

router = routers.DefaultRouter()

router.register(r"tasks", TaskViewSet)
# router.register(r"tasks/(?P<pk>\d+)", TaskViewSet)

router.register(r"task-categories", TaskCategoryViewSet)
# router.register(r"categories/?<pk>\d+", TaskCategoryViewSet)

print(router.urls)
