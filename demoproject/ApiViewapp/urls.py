from django.urls import path
from .views import *

urlpatterns = [
    path('CategoryAPIView/', CategoryAPIView.as_view(), name="CategoryAPIView/"),
    path('CategoryAPIView/<int:pk>/',CategoryAPIView.as_view(), name="CategoryAPIView/"),
]