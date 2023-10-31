from django.urls import path
from .views import *

urlpatterns = [
    path("", LoginView.as_view(), name="login-view"),
    path("register/", RegisterView.as_view(), name="register-view"),
    path("logout/", LogoutView.as_view(), name="logout-view"),
    path("home/", QuestionView.as_view(), name="question-view"),
]