from django.shortcuts import render, get_list_or_404
from .models import Actualite, Anoter, Bienvenue


def index(request):
    actualite = get_list_or_404(Actualite)
    aNoter = get_list_or_404(Anoter)
    bienvenue = get_list_or_404(Bienvenue)
    context = {'actualite': actualite[:3],      # Return first X amount
               'aNoter': aNoter[3:],            # !Limit to latest (3)!
               'bienvenue': bienvenue
               }
    return render(request, 'stLeon/main.html', context)

