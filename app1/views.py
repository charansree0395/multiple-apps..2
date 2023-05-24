from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def first(request):
    return HttpResponse("this is application one first view")

def second(request):
    return HttpResponse("this is application1 second view")