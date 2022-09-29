from rest_framework import serializers
from .models import *
# from drf_extra_fields.fields import Base64ImageField

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class SubCategorySerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # image = Base64ImageField(required=True)
    class Meta:
        model  = SubCategory
        fields = '__all__'