from django.urls import path
from .views import api_register_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register", api_register_view, name="register"),
    path("login2", obtain_auth_token, name="login")
]

