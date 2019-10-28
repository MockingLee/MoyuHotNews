from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .Serializers import NewsSerializer
from .models import News
from rest_framework.response import Response
from django.db.models import Max
from django.http import JsonResponse
# Create your views here.

def index(request):
  print(request)
  return HttpResponse('Hey! Server is running.')

@api_view(['GET'])
def getLastTypeNews(request):
  if 'type' not in request.GET:
    return JsonResponse({
      'code' : 400,
      'msg' : '缺少请求参数type'
    })
  type = request.GET['type']
  obj = News.objects.filter(site_type=type)
  max_generation = obj.aggregate(Max('generation'))
  # print(getLastTypeNews)

  obj = obj.filter(generation=max_generation['generation__max']).order_by("rank")
  serializer = NewsSerializer(obj, many=True)
  return JsonResponse({
    'code' : 200,
    'msg' : '请求' + type + '站点成功',
    'data' : serializer.data
  })

@api_view(['GET'])
def getType(request):
  obj = News.objects.values('site_type').distinct()
  return JsonResponse({
    'code' : 200,
    'msg' : '请求站点列表成功',
    'data' : list(obj.all())
  })
