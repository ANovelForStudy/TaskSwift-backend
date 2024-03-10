from rest_framework import permissions


class TaskPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        pass


class CategoryPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        pass
