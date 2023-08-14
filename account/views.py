from django.contrib import messages
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import *
from .forms import *
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import FileResponse
import qrcode
from geopy.geocoders import Nominatim
from PIL import Image
import requests
import time
import re


def qr_gen(request):
    return FileResponse(open('./static/qr.png', 'rb'), as_attachment=True)

# Create your views here.


class Index(CreateView):
    template_name = 'core/index.html'
    categories = ServiceModel.objects.all()[0:3]
    featured = BlogModel.objects.all()[0:3]
    form_class = PostForm
    success_url = "/thankyou/"

    extra_context = {
        'blog_posts': featured,
        'services': categories,
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


class General(TemplateView):
    template_name = 'core/htr_at_home/general.html'


class Aluminium(TemplateView):
    template_name = 'core/htr_at_home/aluminium.html'


class Paper(TemplateView):
    template_name = 'core/htr_at_home/paper.html'


class Plastic(TemplateView):
    template_name = 'core/htr_at_home/plastic.html'


class Glass(TemplateView):
    template_name = 'core/htr_at_home/glass.html'


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        geocoded_addresses = [
            {
                "name": "45, Saka Tinubu Street, Victoria Island, Lagos",
                "latitude": "6.426203",
                "longitude": "3.422258"
            },
            {
                "name": "Adeniran ogunsanya mall, Surulere, 100242 Lagos",
                "latitude": "6.507965",
                "longitude": "3.351654"
            },
            {
                "name": "Plot 7, Admiralty way, Lekki phase 1, Lagos, 100242 Lagos",
                "latitude": "6.431242",
                "longitude": "3.458567"
            },
            {
                "name": "13 Park Lane Apapa Lagos State, 100242 Lagos",
                "latitude": "6.449186",
                "longitude": "3.382662"
            },
            {
                "name": "Sweet Sensation building, Awolowo road Ikoyi, Lagos State, 100242, Lagos, Nigeria.",
                "latitude": "6.454750",
                "longitude": "3.439200"
            },
            {
                "name": "53, Pump and fell Ado road Ajah Lagos, 100242 Lagos",
                "latitude": "6.462748",
                "longitude": "3.567250"
            },
            {
                "name": "Ikeja City Mall, Alausa, Lagos, 100242 Lagos",
                "latitude": "6.590139",
                "longitude": "3.353070"
            },
            {
                "name": "No 9, Keffi Street off Awolowo road Ikoyi, Lagos State, 100242 Lagos",
                "latitude": "6.440416",
                "longitude": "3.435202"
            },
            {
                "name": "34A Fola Osibo, Lekki Phase 1 Lagos, 100242 Lagos",
                "latitude": "6.424085",
                "longitude": "3.439628"
            },
            {
                "name": "12 Idowu Martins Street VI, Lagos State, 100242 Lagos",
                "latitude": "6.428137",
                "longitude": "3.421138"
            },
            {
                "name": "29 Isaac John Street, G.R.A Ikeja, Lagos, 100242 Lagos",
                "latitude": "6.572282",
                "longitude": "3.356661"
            },
            {
                "name": "Departure Hall MMA2 Ikeja Lagos, 100242 Lagos",
                "latitude": "6.577655",
                "longitude": "3.323942"
            },
            {
                "name": "45 Ogudu Ojota, GRA Lagos State, 100242 Lagos",
                "latitude": "6.577415",
                "longitude": "3.388243"
            },
            {
                "name": "The Palms Lekki, 1 BIS Way Lekki Lagos, 100242 Lagos",
                "latitude": "6.428937",
                "longitude": "3.452775"
            },
            {
                "name": "45 Saka Tinubu VI, Lagos State, 100242 Lagos",
                "latitude": "6.431182",
                "longitude": "3.418467"
            },
            {
                "name": "1463 mall Sanusi Fanfunwa VI Lagos, 100242 Lagos",
                "latitude": "6.429463",
                "longitude": "3.419117"
            },
            {
                "name": "Shoppers Delite, 58 Ademola Adetokunbo VI, Lagos, 100242 Lagos",
                "latitude": "6.434686",
                "longitude": "3.423970"
            },
            {
                "name": "TFC Building, 22 road Festac Lagos State, 100242 Lagos",
                "latitude": "6.474295",
                "longitude": "3.296982"
            },
            {
                "name": "Novare Mall (Sangotedo)-  CNR of Lekki expressway and Monastery road, Sangotedo, 100242 Lagos",
                "latitude": "6.468900",
                "longitude": "3.552769"
            },
            {
                "name": "11, Agungi Ajiran Road (Shepard's place) Agungi, Lagos., 100242 Lagos",
                "latitude": "6.435520",
                "longitude": "3.487203"
            },
            {
                "name": "107 Adeniyi Jones Ikeja Lagos State, 100242 Lagos",
                "latitude": "6.584019",
                "longitude": "3.361175"
            },
            {
                "name": "350/360 Ikorodu road Maryland, Lagos., 100242 Lagos",
                "latitude": "6.557255",
                "longitude": "3.379336"
            },
            {
                "name": "No:6, Chevron Drive, Lekki Peninsula, Lagos State, 100242 Lagos",
                "latitude": "6.450137",
                "longitude": "3.480661"
            },
            {
                "name": "52 Opebi Road Ikeja Lagos State, 100242 Lagos",
                "latitude": "6.580963",
                "longitude": "3.356678"
            },
            {
                "name": "Tantalizers, Mayfair Gardens, Awoyaya Lekki, Lagos, 100242 Lagos",
                "latitude": "6.491286",
                "longitude": "3.598911"
            },
            {
                "name": "Plot 2 Admirlaty Way Lekki Phase 1, 100242 Lagos",
                "latitude": "6.428600",
                "longitude": "3.443184"
            },
            {
                "name": "No 5 Oriwu road (By Petrocam Filling Station(Main street to Whitesand school’s street), 100242 Lagos",
                "latitude": "6.453723",
                "longitude": "3.391490"
            },
            {
                "name": "Booking Lounge MMAII Lagos, 100242 Lagos",
                "latitude": "6.577243",
                "longitude": "3.323907"
            },
            {
                "name": "113, Ogunlana Drive Surulere, 100242 Lagos",
                "latitude": "6.519259",
                "longitude": "3.360647"
            },
            {
                "name": "57 Adekunle Banjo Street off CMD Road, 100242 Lagos",
                "latitude": "6.599773",
                "longitude": "3.361041"
            },
            {
                "name": "Landmark Mall, VI, Lagos, 100242 Lagos",
                "latitude": "6.426859",
                "longitude": "3.422931"
            },
            {
                "name": "Entourage Mall, Adebayo Doherty street, Lekki, Lagos, 100242 Lagos",
                "latitude": "6.431248",
                "longitude": "3.443755"
            },
            {
                "name": "22, Simbiat Abiola Way, Ikeja, 100242 Lagos",
                "latitude": "6.580918",
                "longitude": "3.350379"
            },
            {
                "name": "Orchid road, after Chevron second toll gate, off Lekki- Epe expressway, Lagos, 105102 Lagos",
                "latitude": "6.409989",
                "longitude": "3.559352"
            },
            {
                "name": "52 Abeni plaza, Ligali-Ayorinde street, beside KFC, VI, Lagos., 101241 Victoria island, Lagos",
                "latitude": "6.428029",
                "longitude": "3.414775"
            },
            {
                "name": "The Bloc, 70 Kusenla street, Ikate-Elegushi, off Lekki-Epe expressway, Lagos., 105102 Lagos",
                "latitude": "6.431000",
                "longitude": "3.525713"
            },
            {
                "name": "32 Emmanuel Keshi street, Magodo, Lagos, 100248 Lagos",
                "latitude": "6.601378",
                "longitude": "3.373211"
            },
            {
                "name": "Ologolo street by Dominoes plaza opposite Agungi, off Lekki-Epe expressway, Lagos, 105102 Lagos",
                "latitude": "6.423798",
                "longitude": "3.488287"
            },
            {
                "name": "20A U.B.A road off chevron drive, off Lekki-Epe expressway, Lagos, 105102 Lagos",
                "latitude": "6.433689",
                "longitude": "3.487287"
            },
            {
                "name": "11 Osolo way, Ajao estate, Lagos., 100263 Lagos",
                "latitude": "6.570682",
                "longitude": "3.317264"
            },
            {
                "name": "Plot 310, oworosoki expressway, Gbagada, Lagos., 100234 Lagos",
                "latitude": "6.554204",
                "longitude": "3.396592"
            },
            {
                "name": "15 Ododuwa way Ikeja GRA lagos, 100217 Lagos, Ikeja",
                "latitude": "6.587828",
                "longitude": "3.353236"
            },
            {
                "name": "168 Awolowo Road, ikoyi, 101233 Lagos",
                "latitude": "6.447955",
                "longitude": "3.439246"
            },
            {
                "name": "37, Glover road, 101223 Lagos",
                "latitude": "6.436572",
                "longitude": "3.425948"
            },
            {
                "name": "68 Admiralty way besides D'wine bank, Lekki Phase 1, Lagos, 105102 Lagos",
                "latitude": "6.433180",
                "longitude": "3.453047"
            },
            {
                "name": "Woolworth Plaza, 307 Adeola Odeku St, Victoria Island, Lagos, 101241 Lagos",
                "latitude": "6.428110",
                "longitude": "3.418695"
            },
            {
                "name": "Housing Estate, victoria island, 101241 Lagos",
                "latitude": "6.428196",
                "longitude": "3.418237"
            },
            {
                "name": "10a Admiralty way Lekki phase 1 opposite Ever Care Hospital, 100242 Lagos",
                "latitude": "6.427301",
                "longitude": "3.428163"
            },
            {
                "name": "Ogudu city mall, 175 Ogudu Road, Ojota, Lagos, 100242 Lagos",
                "latitude": "6.572171",
                "longitude": "3.385031"
            },
            {
                "name": "Block 113 Plot 1c, Corner-piece property on Hakeem Dickson street, Lekki Phase 1, Lagos., 105102 Lagos",
                "latitude": "6.432109",
                "longitude": "3.440021"
            },
            {
                "name": "26, Adeola Hopewell Street, Victoria Island, Lagos, 100001 Lagos",
                "latitude": "6.428997",
                "longitude": "3.418469"
            },
            {
                "name": "107 Allen Avenue, Ikeja, Lagos, 1000001 Lagos",
                "latitude": "6.608371",
                "longitude": "3.352358"
            },
            {
                "name": "Plot 1 and 10 Akiogun Road, Oniru, Lekki, Lagos, 1000001 Lagos",
                "latitude": "6.437148",
                "longitude": "3.448206"
            },
            {
                "name": "Ikota Retail Store, beside Mega Chicken, Ikota, Lagos, 1000001 Lagos",
                "latitude": "6.464306",
                "longitude": "3.570287"
            },
            {
                "name": "Shop B4 and B5, Capital Garden Mall, Orchid Hotel Road, Eti-Osa, Lagos, 1000001 Lagos",
                "latitude": "6.435152",
                "longitude": "3.547051"
            },
            {
                "name": "Shop B, Ground Floor, Mobolaji Johnson Railway Station, Lagos, 1000001 Lagos",
                "latitude": "6.456739",
                "longitude": "3.409409"
            },
            {
                "name": "12, Fola Osibo Road, Lekki Phase 1, 1000001 Lagos",
                "latitude": "6.424506",
                "longitude": "3.439315"
            },
            {
                "name": "10, Adeola Odeku Street, Victoria Island, 1000001 Lagos",
                "latitude": "6.427585",
                "longitude": "3.418095"
            },
            {
                "name": "22 Road, Festac, Lagos, 1000001 Lagos",
                "latitude": "6.490157",
                "longitude": "3.279700"
            },
            {
                "name": "New International Terminal of Murtala Muhammed International Airport, Ikeja , Lagos, 1000001 Lagos",
                "latitude": "6.576446",
                "longitude": "3.321727"
            },
            {
                "name": "8A, Kingsway Road, Ikoyi, Lagos, 1000001 Lagos",
                "latitude": "6.443113",
                "longitude": "3.424682"
            },
            {
                "name": "BNB Mall, Lakowe Golf, Ibeju Lekki, Lagos, 1000001 Lagos",
                "latitude": "6.457225",
                "longitude": "3.710129"
            },
            {
                "name": "38, Salami Suaibu Street, Pedro Road, Palmgroove, Lagos, 1000001 Lagos",
                "latitude": "6.534342",
                "longitude": "3.378012"
            },
            {
                "name": "Kingsbite, British America Junction, Jos, Plateau State, 1000001 Plateau",
                "latitude": "9.929802",
                "longitude": "8.885753"
            },
            {
                "name": "4, Old Aba Road, Rumuomasi, Port Harcourt, 1000001 Lagos",
                "latitude": "4.844197",
                "longitude": "7.031204"
            },
            {
                "name": "iFitness - Lekki Expressway, Jakande, Busstop, Lagos State, 1000001 Lagos",
                "latitude": "6.482369",
                "longitude": "3.571997"
            },
            {
                "name": "Cubana World, 17 Adeola Odeku Street, Victoria Island, 1000001 Lagos",
                "latitude": "6.427921",
                "longitude": "3.418423"
            },
            {
                "name": "1 Muhammed Street, Santos Layout, Akonwonjo R/about, Ikeja, Lagos, 1000001 Lagos",
                "latitude": "6.614195",
                "longitude": "3.308170"
            },
            {
                "name": "31, Awolowo Road, Ikoyi, Lagos, 1000001 Lagos",
                "latitude": "6.440453",
                "longitude": "3.420772"
            },
            {
                "name": "Hypercity Supermarket; 27 Awoke Street, Nkpogu, Port- Harcourt, 1000001 Lagos",
                "latitude": "4.825496",
                "longitude": "7.007570"
            },
            {
                "name": "Block XXI, Plot 19, Chief Yesufu Abiodun Way/ Lawani Oduloye Road, Oniru Estate, Lekki, 100001 Lekki",
                "latitude": "6.430127",
                "longitude": "3.442399"
            },
            {
                "name": "No 131 Obafemi Awolowo Way, Ikeja, Lagos, 100001 Lekki",
                "latitude": "6.570476",
                "longitude": "3.366667"
            },
            {
                "name": "No 6, Chevron Drive, Lekki Pennisula, 12825 Lekki",
                "latitude": "6.449864",
                "longitude": "3.470917"
            },
            {
                "name": "Block 138, Plot 8 Lekki Scheme 1, Lagos, 1000001 Lagos",
                "latitude": "6.432171",
                "longitude": "3.441135"
            },
            {
                "name": "Ranbrook Square, No 2, Baale street, Igbo-efon busstop, lekki, lagos, 1000001 Lagos",
                "latitude": "6.420554",
                "longitude": "3.493222"
            },
        ]
        context['geocoded_addresses'] = geocoded_addresses
        return context


class NearbyRecyclingCentresSearch(ListView):
    model = CollectionCenterModel
    template_name = 'collection/search_result.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = self.model.objects.all()
        object_list = object_list.filter(Q(name__icontains=query) | Q(
            full_address__icontains=query) | Q(state__icontains=query))
        return object_list


class NearbyRecyclingCentresDetail(DetailView):
    model = CollectionCenterModel
    template_name = 'collection/nearby_recycling_centres_detail.html'


class NearbyRecyclingCentresCreate(CreateView):
    model = CollectionCenterModel
    template_name = 'collection/nearby_recycling_centres_create.html'
    form_class = CollectionCenterForm
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
