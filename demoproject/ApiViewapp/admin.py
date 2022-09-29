from socket import CAN_EFF_FLAG
from django.contrib import admin
from .models import *
# Register your models here.

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Category)
admin.site.register(SubCategory,SubcategoryAdmin)

