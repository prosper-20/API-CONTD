from django.urls import path
from .views import HomePage, DetailPage, CreateNewPage, EditNewsPage, DeleteNewsPage

urlpatterns = [
    path('<int:pk>/', DetailPage.as_view(), name='details'),
    path('<int:pk>/delete/', DeleteNewsPage.as_view(), name='delete'),
    path ('<int:pk>/edit/', EditNewsPage.as_view(), name='edit'),
    path ('create/', CreateNewPage.as_view(), name='create'),
    path('', HomePage.as_view(), name='home'),
    
    
    
]