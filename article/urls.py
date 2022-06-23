from django.urls import path, include

from rest_framework import routers
from .views import ArticleViewSet

router = routers.SimpleRouter()
router.register(r'', ArticleViewSet, basename='article')
urlpatterns = [
    path('', include(router.urls)),
]
