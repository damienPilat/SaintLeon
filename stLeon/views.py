from django.shortcuts import render, get_list_or_404
from .models import Actualite, Anoter, Bienvenue, Batiments


def index(request):
    actualite = get_list_or_404(Actualite)
    aNoter = get_list_or_404(Anoter)
    bienvenue = get_list_or_404(Bienvenue)
    horairesMesse = getHorairesMesse()
    context = {'actualite': actualite[:3],      # Return first X amount
               'aNoter': aNoter,            # !Limit to latest (3)!
               'bienvenue': bienvenue,
               'horairesMesse': horairesMesse
               }
    return render(request, 'stLeon/main.html', context)


def test(request):
    bienvenue = get_list_or_404(Bienvenue)
    aNoter = get_list_or_404(Anoter)
    horairesMesse = getHorairesMesse()
    context = {'bienvenue': bienvenue,
               'aNoter': aNoter,
               'horairesMesse': horairesMesse}
    return render(request, 'stLeon/test.html', context)


def test_2(request):
    batiments = get_list_or_404(Batiments)
    context = {'batiments': batiments}
    return render(request, 'stLeon/test_2.html', context)


def getHorairesMesse():
    return 'stLeon/images/horaires_messe_HorsVacances.png'
