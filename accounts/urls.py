from django.urls import path, include
from .views import RegisterView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]