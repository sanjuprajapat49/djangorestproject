from ast import ExceptHandler
from django.shortcuts import render
from requests import post
# from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ViewSet
from ApiViewapp.models import *
from ApiViewapp.serializers import *
from rest_framework.response import Response
# from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
# Create your views here.

class SCAPIView(ViewSet):
    parser_classes = (MultiPartParser, )
    # parser_classes = [JSONParser]
    # parser_classes = (MultiPartParser,FormParser,JSONParser)


    # parser_classes = (FormParser, MultiPartParser)
    def list(self, request, format=None):
        subcat = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcat, many=True)
        return Response({'status':200,'data':serializer.data})
    
    @swagger_auto_schema(request_body=SubCategorySerializer,operation_description="Create Subcategory API",responses={200:'success'})
    def create(self, request, format=None):
        # breakpoint()
        try:
            serializer = SubCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'data':serializer.data,'message':'data created successfully...'})
            else:
                return Response({'error':serializer.errors,'message':'something went wrong wrong...'})
        except Exception as e:
            return Response({'error':e,'message':'something went wrong...'})
    
    def retrieve(self, request, pk=None,format=None):
        try:
            subcat = SubCategory.objects.get(id=pk)
            serializer = SubCategorySerializer(subcat)
            return Response({'status':200,'data':serializer.data})
        except Exception as e:
            return Response({'errors':e,'message':'something went wrong...'})