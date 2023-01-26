from django.contrib import messages
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import *
from .forms import *
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render,redirect

# Create your views here.
class Index(CreateView):
    template_name = 'core/index.html'
    categories = ServiceModel.objects.all()[0:3]
    featured = BlogModel.objects.all()[0:3]
    form_class = PostForm
    success_url = "/thankyou/"
    
    extra_context = {
        'blog_posts': featured,
        'services':categories,
    }

   
class Faq(TemplateView):
    template_name = 'core/faq.html'
    
class ThankYou(TemplateView):
    template_name = 'core/thank_you.html'
   
class Contact(CreateView):
    template_name = 'core/contact.html'
    form_class = ConactForm
    success_url = "/thankyou/"

class GeneralInformationOnRecycling(TemplateView):
    template_name = 'core/general_information_on_recycling.html'
    

class HowToRecycleAtHome(TemplateView):
    template_name = 'core/how_to_recycle_at_home.html'


class AboutUs(TemplateView):
    template_name = 'core/about.html'


class Blog(ListView):
     model = BlogModel
     template_name = 'blog/blog.html'
     paginate_by = 10

class BlogDetail(DetailView):
    model = BlogModel
    template_name = 'blog/blog_detail.html'
    
    
class NearbyRecyclingCentres(ListView):
    model = CollectionCenterModel
    template_name = 'collection/nearby_recycling_centres.html'
    paginate_by = 10
    
    
class NearbyRecyclingCentresSearch(ListView):
    model = CollectionCenterModel
    template_name = 'collection/search_result.html'
    paginate_by = 10
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = self.model.objects.all()
        object_list = object_list.filter(Q(name__icontains=query) | Q(full_address__icontains=query)| Q(state__icontains=query))
        return object_list
    
   
class NearbyRecyclingCentresDetail(DetailView):
    model = CollectionCenterModel
    template_name = 'collection/nearby_recycling_centres_detail.html' 

class NearbyRecyclingCentresCreate(CreateView):
    model = CollectionCenterModel
    fields = ['name','number','whats_app','state','google_map_link','full_address','opening_time','closing_time','pricing',]
    template_name = 'collection/nearby_recycling_centres_create.html' 
    form_class = PostForm
    success_url = "/thankyou/"

class Services(ListView):
    model = ServiceModel
    template_name = 'core/services.html'

class ServiceDetail(DetailView):
    model = ServiceModel
    template_name = 'core/services_detail.html'
    
class BecomeAnAgent(CreateView):
    template_name = 'agent/become_an_agent.html'
    model = BecomeAnAgent
    form_class = BecomeAnAgentForm
    success_url = "/thankyou/"

def error_404(request, exception):
    return render(request, '404.html')