
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render

from .models import *

def index(request):
    return render(request, 'mainRest/index.html')
