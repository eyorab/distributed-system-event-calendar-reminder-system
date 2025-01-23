from django.urls import path
from . import views
from . import api_views
urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signUp, name="signup"),
    path("profile/", views.profile, name="profile"),
    #api urls
    path("api/users/", api_views.UserAPIView.as_view(), name="user-api"),
    path("api/users/login/", api_views.UserLoginAPIView.as_view(), name="user-login"),
]