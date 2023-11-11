from django.shortcuts import render
from django.http import HttpResponse
from .raw_data import retrive_data
from .preprocessing import preprocess_pipeline
from rest_framework import status
import json
from .serializers import tagSerializers,preprocessedcourseSerializers
from .models import tag,preprocessedcourse
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .Add_Fuct import cosine_indices_maker
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

def preprocess_data(request,table_name):
    status = preprocess_pipeline(table_name)
    return HttpResponse(json.dumps(status))

@api_view(['GET'])
def data_show_preprocessed(request,table_name):
    if table_name == 'course_list':
        course_list = preprocessedcourse.objects.all()[:5]
        serializer = preprocessedcourseSerializers(course_list,many=True)
        return Response(serializer.data)
    else:
        return Response(status.HTTP_400_BAD_REQUEST)

def cosine_sim_indices_maker(request):
    status = cosine_indices_maker()
    return HttpResponse(json.dumps(status))

