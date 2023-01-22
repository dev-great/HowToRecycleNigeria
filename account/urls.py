from django.urls import path, include
from .views import *

app_name = 'account'

urlpatterns = [
    path('', Index.as_view(), name="home_page"),
]