'''from django.urls import path

app_name = 'articles'
urlpatterns = [
    path('articles/create/', ArticlesCreateView.as_view()),
    path('articles/all/', ArticlesListView.as_view()),
    path('articles/private/', ArticlesPrivateListView.as_view()),
    path('articles/detail/<int:pk>/', ArticlesDetailView.as_view()),
    path('registr/', RegistrUserView.as_view()),
]
'''

from rest_framework import routers
from .views import ArticleViewSet

router = routers.SimpleRouter()
router.register(r'article', ArticleViewSet)
urlpatterns = router.urls