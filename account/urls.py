from django.urls import path, include
from .views import *

app_name = 'account'

urlpatterns = [
    path('', Index.as_view(), name="home_page"),
    path('become_an_agent/', BecomeAnAgent.as_view(), name="become_an_agent" ),
]