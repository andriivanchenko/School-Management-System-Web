from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import login_view, ProfileView

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile")
]
