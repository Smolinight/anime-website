from django.urls import path 
from .views import *

urlpatterns = [
    path('', index),
    path('anime_list/', anime_list),
]