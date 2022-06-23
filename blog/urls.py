from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/register/', include('users.urls')),
    path('api/v1/article/', include('article.urls')),
]
