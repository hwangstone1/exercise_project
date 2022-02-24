from django.shortcuts import render
from django.http import request, HttpResponse
# Create your views here.

def main(request):
    return HttpResponse("hello")
