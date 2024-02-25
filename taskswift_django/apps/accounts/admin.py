from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Admin, CustomUser, Employee, Manager


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                ),
            },
        ),
        (
            "Персональная информация",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "gender",
                    "address",
                    "date_of_birth",
                    "skills",
                    "bio",
                    "social_links",
                ),
            },
        ),
        (
            "Контакты для экстренных случаев",
            {
                "fields": (
                    "emergency_contact_name",
                    "emergency_contact_phone",
                ),
            },
        ),
        (
            "Разрешения",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Важные даты",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "phone",
                ),
            },
        ),
    )
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Employee)
admin.site.register(Manager)


# @admin.register()
# class ProfileModelAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "user",
#         "get_first_name",
#         "get_last_name",
#         "gender",
#         "phone",
#         "emergency_contact_phone",
#         "address",
#         "date_of_birth",
#         "date_joined",
#         "created_at",
#         "updated_at",
#     )

#     list_filter = (
#         "gender",
#         "date_of_birth",
#         "date_joined",
#         "created_at",
#         "updated_at",
#     )

#     search_fields = (
#         "phone",
#         # ""
#     )

#     def get_first_name(self, obj):
#         return obj.user.first_name

#     get_first_name.short_description = "Имя"
#     get_first_name.admin_order_field = "user__first_name"

#     def get_last_name(self, obj):
#         return obj.user.last_name

#     get_last_name.short_description = "Фамилия"
#     get_last_name.admin_order_field = "user__last_name"
