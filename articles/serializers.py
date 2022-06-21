from rest_framework import serializers
from .models import Articles, CustomUser
from django.contrib.auth import password_validation
from django.core.validators import validate_email


class ArticlesRegistrSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def validate(self, data):
        password_validation.validate_password(data['password'])
        validate_email(data['email'])

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=self.validated_data['email'],
            password=self.validated_data['password']
        )
        return user


class ArticlesListSerializers(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Articles
        fields = '__all__'


class ArticlesDetailSerializers(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Articles
        fields = '__all__'


class ArticlesPrivateListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
