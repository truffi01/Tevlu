from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def homePage(req):
    return HttpResponse('First App')

class HomePage (TemplateView):
    template_name = 'home.html'

class CreateUser (TemplateView):
    template_name = 'createUser.html'