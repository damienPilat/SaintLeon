from django.db import models
from django.core.validators import RegexValidator


# List des Actualités
class Actualite(models.Model):
    titre = models.CharField(max_length=500)
    text = models.TextField(max_length=5000)        # RECOGNISE LINE BREAK
    date = models.DateTimeField('date ajouter')
    link = models.CharField(max_length=2048)
    first_element = models.BooleanField(default=False)
    last_element = models.BooleanField(default=False)

    def __str__(self):
        return self.titre


# List des elements À Noter
class Anoter(models.Model):
    titre = models.CharField(max_length=500)
    text = models.TextField(max_length=5000)
    date = models.DateTimeField('date ajouter')
    link = models.CharField(max_length=2048)
    img_src = models.CharField(max_length=500)

    def __str__(self):
        return self.titre


# Elements de Bienvenue
class Bienvenue(models.Model):
    text = models.TextField(max_length=5000)
    img_src = models.CharField(max_length=500, blank=True, default=None)


# List des Batiments à Saint-Léon
class Batiments(models.Model):
    nom = models.CharField(max_length=500, default='')
    text = models.TextField(max_length=5000)
    img_src = models.CharField(max_length=500)

    def __str__(self):
        return self.nom


# List des Communautes Religieuse
class Religieuse(models.Model):
    nom = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    desc = models.TextField(max_length=5000)
    img_src = models.CharField(max_length=500)
    site = models.CharField(max_length=500)

    def __str__(self):
        return self.nom
