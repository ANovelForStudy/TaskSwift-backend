from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, User

# Register your models here.
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "get_first_name",
        "get_last_name",
        # "get_profile_first_name",
        "gender",
        "phone",
        "emergency_contact_phone",
        "address",
        "date_of_birth",
        "date_joined",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "gender",
        "date_of_birth",
        "date_joined",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "phone",
        # ""
    )

    def get_first_name(self, obj):
        return obj.user.first_name

    get_first_name.short_description = "Имя"
    get_first_name.admin_order_field = "user__first_name"

    def get_last_name(self, obj):
        return obj.user.last_name

    get_last_name.short_description = "Фамилия"
    get_last_name.admin_order_field = "user__last_name"
