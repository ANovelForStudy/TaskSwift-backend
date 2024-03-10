from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers

from users.models import CustomUser

REGISTRATION_FIELD_SET = [
    "id",
    "first_name",
    "last_name",
    "password",
    "email",
    "user_type",
]

FIELD_SET = [
    "id",
    "first_name",
    "middle_name",
    "last_name",
    "email",
    "user_type",
    "gender",
    "address",
    "phone",
    "date_of_birth",
    "date_joined",
    "skills",
    "bio",
    "social_links",
    "emergency_contact_name",
    "emergency_contact_phone",
    "profile_picture",
    "created_at",
    "updated_at",
]


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = FIELD_SET


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = REGISTRATION_FIELD_SET


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = FIELD_SET
