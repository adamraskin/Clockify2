from django.shortcuts import render
from django.http import HttpResponse

def graph(request):
    return HttpResponse("Clockify2 graphs")