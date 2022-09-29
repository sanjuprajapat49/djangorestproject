from django.shortcuts import render
from django.http import JsonResponse
from ApiViewapp.models import *
from django.core.cache import cache
# Create your views here.


def home(request):
    payload = []
    db = None
    if cache.get('fruits'):
        payload = cache.get('fruits')
        db = 'redis'
        data_expire_in = cache.ttl('fruits')
    else:
        categories = Category.objects.all()
        for i in categories:
            payload.append(i.name)
        db = 'postgres'
        cache.set('fruits',payload,timeout=1024)
        # cache.set('fruits',payload)
        data_expire_in = None

    return JsonResponse({'status':200,'db':db, 'data':payload,'expire_time':data_expire_in})