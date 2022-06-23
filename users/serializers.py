from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import password_validation
from django.core.validators import validate_email


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def validate(self, data):
        password_validation.validate_password(data['password'])
        validate_email(data['email'])
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=self.validated_data['email'],
            password=self.validated_data['password'],
        )
        return user
