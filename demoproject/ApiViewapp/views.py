# from django.shortcuts import render
from functools import partial
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

"""
    --------------------swagger doc---------------------------------
    
    swagger ui customization:
    swagger_schema = None # is used for hide the apis from swagger ui
    
    @swagger_auto_schema also used for customization
    
    @swagger get parameters are:
    
    1. operation_description = ""
    2. responses = {}

"""


class CategoryAPIView(APIView):
    # swagger_schema = None
    @swagger_auto_schema(operation_description="This Api provide the all categories", responses={200:"success"})
    def get(self, request,pk=None,format=None):
        try:
            if pk is not None:
                category = Category.objects.get(id=pk)
                serializer = CategorySerializer(category)
                return Response({'status':200,'data':serializer.data})
            else:
                category = Category.objects.all()
                serializer = CategorySerializer(category, many=True)
                return Response({'status':200,'data':serializer.data})
        except Exception as e:
            return Response({'error':e,'message':'something went wrong...'})
    
    def post(self, request, format=None):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'data':serializer.data,'message':"data created successfully"})
            else:
                return Response({"status":serializer.errors, "message":'something went wrong'})
        except Exception as e:
            return Response({'errors':e,"message":"something went wrong"})
        
    def put(self, request, pk=None, format=None):
        try:
            category = Category.objects.get(id=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200, 'data': serializer.data, 'message':'data successfully updated...'})
            else:
                return Response({'status':serializer.errors,'message':'something went wrong'})
        except Exception as e:
            return Response({'errors':e,"message":'something went wrong...'})
    
    def patch(self, request, pk=None, format=None):
        try:
            category = Category.objects.get(id=pk)
            serializer = CategorySerializer(category, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200, 'data': serializer.data, 'message':'data partially successfully updated...'})
            else:
                return Response({'status':serializer.errors,'message':'something went wrong'})
        except Exception as e:
            return Response({'errors':e,"message":'something went wrong...'})
        
    def delete(self, request, pk=None, format=None):
        try:
            category = Category.objects.get(id=pk)
            category.delete()
            return Response({'status':200,'message':'data successfully deleted...'})
        except Exception as e:
            return Response({'errors':e,'message':'something went wrong...'})
        
    