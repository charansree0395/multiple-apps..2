from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def a2_first(rquest):
    return HttpResponse("This is an application 2 first view")

def a2_second(request):
    return HttpResponse("This is an application 2 in second view")