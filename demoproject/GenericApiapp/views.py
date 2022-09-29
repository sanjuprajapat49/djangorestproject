from django.shortcuts import render
from ApiViewapp.models import *
from ApiViewapp.serializers import *
# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
# from rest_framework.mixins import ListCreateModelMixin

from drf_yasg.utils import swagger_auto_schema

"""
    --------------------swagger doc---------------------------------
    
    swagger ui customization:
    swagger_schema = None # is user for hide the apis from swagger ui

"""

class CategoryDataApiView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self,request,*args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class GenericDetailApiView(GenericAPIView,UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # breakpoint()
    def get(self,request,*args,**kwargs):
        # breakpoint()        
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

# class ApiView(GenericAPIView)