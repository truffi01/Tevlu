from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(req):
    return HttpResponse('First App')