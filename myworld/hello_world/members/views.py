from django.shortcuts import render
from django.http import HttpResponse

def members(request):  # Name of function can be anything
    return HttpResponse("Hello world!")