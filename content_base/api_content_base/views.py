from django.shortcuts import render
from django.http import HttpResponse
from .raw_data import retrive_data
from django.http import HttpRequest as request
import json
# Create your views here.

from rest_framework.decorators import api_view
@api_view(['GET'])
def data_retrival(request,table_name):
    status = retrive_data(table_name)
    return HttpResponse(json.dumps(status))

def index(request):
    return HttpResponse("This is index page")