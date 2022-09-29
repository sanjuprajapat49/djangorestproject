from nturl2path import url2pathname
from django.urls import path
from .views import *
urlpatterns = [
    path('CategoryDataApiView/',CategoryDataApiView.as_view(),name="CategoryDataApiView/"),
    path('GenericDetailApiView/<int:pk>/',GenericDetailApiView.as_view()), 
]
