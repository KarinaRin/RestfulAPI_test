from .serializers import *
from .models import Article
from rest_framework import viewsets
from users.permissions import *


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthor, ]
        elif self.action in ('update', 'destroy', 'retrieve'):
            self.permission_classes = [IsAuthorOrReadOnly, ]
        return super(ArticleViewSet, self).get_permissions()

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Article.objects.filter(public=True)
        return Article.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
