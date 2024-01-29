from django.urls import path
from .views import *

urlpatterns = [
    path('bases/', BaseListAPIView.as_view(), name='base-list'),
    path('bases/<int:pk>/', BaseDetailAPIView.as_view(), name='base-detail'),
    path('folders/', FolderListAPIView.as_view(), name='folder-list'),
    path('folders/<int:pk>/', FolderDetailAPIView.as_view(), name='folder-detail'),
]