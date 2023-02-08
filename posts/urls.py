from django.urls import path
from .views import PostList, PostDetail


urlpatterns = [
    path("list/", PostList.as_view(), name="list"),
    path("<int:pk>/", PostDetail.as_view(), name="detail")
]