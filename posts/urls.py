from django.urls import path
from .views import PostList, PostDetail, api_register_view


urlpatterns = [
    path("list/", PostList.as_view(), name="list"),
    path("<int:pk>/", PostDetail.as_view(), name="detail"),
    path("register", api_register_view, name="register")
]