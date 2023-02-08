from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Anime app!")

def anime_list(request):
    return HttpResponse("Список аниме")

