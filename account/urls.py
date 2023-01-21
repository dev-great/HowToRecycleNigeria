from django.urls import path, include
from .views import *
from django.views.decorators.csrf import csrf_protect

app_name = 'account'

urlpatterns = [
    path('dashborad/', views.dashborad , name='dashborad'),
]