from django.urls import path
from .views import RegisterUserView

app_name = 'users'
urlpatterns = [
    path('', RegisterUserView.as_view()),
]
