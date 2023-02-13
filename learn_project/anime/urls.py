from django.urls import path 
from .views import *

urlpatterns = [
    path('', index),
    path('anime_list/<int:animeid>/', anime_list),
    path('persons_list/<slug:person>/', persons_list),
    path('about/', about)
]