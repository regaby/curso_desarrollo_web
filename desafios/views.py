from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Practica python!')

def febrero(request):
    return HttpResponse('Haz ejercicio!')