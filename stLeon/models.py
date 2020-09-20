from django.db import models


class Batiments(models.Model):
    nom = models.CharField(max_length=500)
    sousol = models.CharField(max_length=500)
    entresol = models.CharField(max_length=500)
    premier_etage = models.CharField(max_length=500)
    troisieme_etage = models.CharField(max_length=500)
    quatrieme_etage = models.CharField(max_length=500)

    def str__str__(self):
        return self.nom