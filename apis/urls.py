from django.urls import path
from .views import api_list_page, Api_list_page, Api_detail_view, api_create_page, api_update_page, API_LIST_PAGE

urlpatterns =[
    path("home/", api_list_page, name="api-home"),
    path("class/home/", Api_list_page.as_view(), name="api-class-home"),
    path("class/detail/<slug:slug>/", Api_detail_view.as_view(), name="class-detail"),
    path("create/", api_create_page, name="api-create"),
    path("<slug:slug>/update/", api_update_page, name="update"),
    path("class/create/", API_LIST_PAGE.as_view(), name="class-create")
]