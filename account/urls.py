from django.urls import path, include
from .views import *

app_name = 'account'

urlpatterns = [
    path('download_qr/', qr_gen, name="download_qr" ),
    path('', Index.as_view(), name="home_page"),
    path('become_an_agent/', BecomeAnAgent.as_view(), name="become_an_agent" ),
    path('faq/', Faq.as_view(), name="faq" ),
    path('contact/', Contact.as_view(), name="contact" ),
    path('general_information_on_recycling/', GeneralInformationOnRecycling.as_view(), name="general_information_on_recycling"),
    path('services/<pk>/', ServiceDetail.as_view(), name="service_detail"),
    path('Services/', Services.as_view(), name="services" ),
    path('about_us/', AboutUs.as_view(), name="about" ),
    path('blog/', Blog.as_view(), name="blog" ),
    path('blog/<pk>/', BlogDetail.as_view(), name="blog_detail" ),
    path('nearby_recycling_centres/', NearbyRecyclingCentres.as_view(), name="nearby_recycling_centres" ),
    path('nearby_recycling_centres/<pk>/', NearbyRecyclingCentresDetail.as_view(), name="nearby_recycling_centres_detail" ),
    path('nearby_recycling_centres_create/', NearbyRecyclingCentresCreate.as_view(), name="nearby_recycling_centres_create" ),
    path('contact/', Contact.as_view(), name="contact" ),
    path('thankyou/', ThankYou.as_view(), name="thankyou" ),
    path('search_result/', NearbyRecyclingCentresSearch.as_view(), name="search_result" ),
    path('how_to_recycle_at_home/general/', General.as_view(), name="general" ),
    path('how_to_recycle_at_home/aluminium/', Aluminium.as_view(), name="aluminium" ),
    path('how_to_recycle_at_home/plastic/', Plastic.as_view(), name="plastic" ),
    path('how_to_recycle_at_home/paper/', Paper.as_view(), name="paper" ),
    path('how_to_recycle_at_home/glass/', Glass.as_view(), name="glass" ),
]