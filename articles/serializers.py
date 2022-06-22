from rest_framework import serializers
from .models import Article


class ArticleSerializers(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = '__all__'
