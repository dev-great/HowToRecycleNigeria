from django.contrib import messages
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import *
from django.shortcuts import render,redirect

# Create your views here.
class Index(TemplateView):
    template_name = 'core/index.html'
   
class Faq(TemplateView):
    template_name = 'core/faq.html'
   
class Contact(TemplateView):
    template_name = 'core/contact.html'

class GeneralInformationOnRecycling(TemplateView):
    template_name = 'core/general_information_on_recycling.html'
    

class HowToRecycleAtHome(TemplateView):
    template_name = 'core/how_to_recycle_at_home.html'


class AboutUs(TemplateView):
    template_name = 'core/about.html'


class Blog(ListView):
     model = BlogModel
     template_name = 'blog/blog.html'
     def get_queryset(self, *args, **kwargs):
        qs = super(Blog, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

class BlogDetail(DetailView):
    model = BlogModel
    template_name = 'blog/blog_detail.html'
    

class NearbyRecyclingCentres(ListView):
    model = CollectionCenterModel
    template_name = 'collection/nearby_recycling_centres.html'
   
class NearbyRecyclingCentresDetail(DetailView):
    model = CollectionCenterModel
    template_name = 'collection/nearby_recycling_centres_detail.html' 

class NearbyRecyclingCentresCreate(CreateView):
    model = CollectionCenterModel
    fields = ['name','number','whats_app','state','google_map_link','full_address','opening_time','closing_time','pricing',]
    template_name = 'collection/nearby_recycling_centres_create.html' 


class Services(ListView):
    model = ServiceModel
    template_name = 'core/services.html'
    
    def get_queryset(self, *args, **kwargs):
        qs = super(Services, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

class ServiceDetail(DetailView):
    model = ServiceModel
    template_name = 'core/services_detail.html'
    
class BecomeAnAgent(CreateView):
    template_name = 'agent/become_an_agent.html'
    model = BecomeAnAgent
    fields = ['name','phoneNumber','state',]

def error_404(request, exception):
    return render(request, '404.html')