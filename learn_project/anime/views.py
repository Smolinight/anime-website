from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = ["About us", "Main page", "Sign in", "Support"]

def index(request):
    animes = Anime.objects.all()
    print(animes)
    return render(request, 'anime/index.html', {'title': 'Anime main page', 'menu': menu, 'animes': animes})

def about(request):
    return render(request, 'anime/about.html', {'title': 'About us', 'menu': menu})

def anime_list(request, animeid):
    return HttpResponse(f"<h1> Список аниме c id: {animeid} </h1>")

def persons_list(request, person):
    p_l = ["Hiroka", "Kaneki", "Kageyama", "Eren"] #типо получаем список пользователей из бд
    if person not in p_l:
        raise Http404() # redirect to pageNotFound func
    return HttpResponse(f"<h1> Герой cо слагом: {person} </h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1> Страница не найдена :( </h1>')