from django.shortcuts import render
from django.http import HttpResponse

def tracker(request):
    return HttpResponse("Clockify2 tracker")