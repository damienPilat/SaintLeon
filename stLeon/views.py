from django.shortcuts import render, get_list_or_404
from .models import Actualite, Anoter, Bienvenue, Batiments, Religieuse


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


def batiments(request):
    batiments = get_list_or_404(Batiments)
    religieuse = get_list_or_404(Religieuse)
    context = {'batiments': batiments,
               'religieuse': religieuse}
    return render(request, 'stLeon/batiments.html', context)


def visite_cult(request):
    return render(request, 'stLeon/visiteCult.html')


def test(request):
    bienvenue = get_list_or_404(Bienvenue)
    aNoter = get_list_or_404(Anoter)
    horairesMesse = getHorairesMesse()
    context = {'bienvenue': bienvenue,
               'aNoter': aNoter,
               'horairesMesse': horairesMesse}
    return render(request, 'stLeon/test.html', context)


def test_3(request):
    religieuse = get_list_or_404(Religieuse)
    context = {'religieuse': religieuse}
    return render(request, 'stLeon/test_3.html', context)


def getHorairesMesse():
    return 'stLeon/images/horaires_messe_HorsVacances.png'
