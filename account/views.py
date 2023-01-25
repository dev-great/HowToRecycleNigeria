from django.contrib import messages
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import *
from django.shortcuts import render,redirect

# Create your views here.
class Index(TemplateView):
    template_name = 'core/index.html'
    

class BecomeAnAgent(CreateView):
    template_name = 'agent/become_an_agent.html'
    model = BecomeAnAgent
    fields = ['name','phoneNumber','state',]

def error_404(request, exception):
    return render(request, '404.html')