from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

# Create your views here.

class HomePage (TemplateView):
    template_name = 'home.html'

class CreateUser (generic.CreateView):
    template_name = 'createUser.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm