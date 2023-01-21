from django.urls import path, include
from .views import *
from django.views.decorators.csrf import csrf_protect

app_name = 'collectioncenter'

urlpatterns = [
    # path('login/', csrf_protect(obtain_auth_token)),
    # path('register/', RegisterView.as_view()),
]