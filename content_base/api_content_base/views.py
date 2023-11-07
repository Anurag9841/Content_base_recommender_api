from django.shortcuts import render
from django.http import HttpResponse
from .raw_data import retrive_data
from rest_framework import status
import json
from .serializers import tagSerializers
from .models import tag
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def data_retrival(request,table_name):
    status = retrive_data(table_name)
    return HttpResponse(json.dumps(status))

@api_view(['GET'])
def data_show(request,table_name):
    if table_name == 'tag':
        tags = tag.objects.all()[:5]
        serializer = tagSerializers(tags,many=True)
        return Response(serializer.data)
    else:
        return Response(status.HTTP_400_BAD_REQUEST)

def index(request):
    return HttpResponse("This is index page")