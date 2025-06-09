from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(f"Welcome to the forum app!")
