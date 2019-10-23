from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .Serializers import NewsSerializer
from .models import News
from rest_framework.response import Response
# Create your views here.

def index(request):
  print(request)
  return HttpResponse('Hey! Server is running.')

@api_view(['GET'])
def getTypeNews(request):
  type = request.GET['type']
  if request.method == 'GET':
    obj = News.objects.filter(site_type=type)
    serializer = NewsSerializer(obj, many=True)
    return Response(serializer.data)
