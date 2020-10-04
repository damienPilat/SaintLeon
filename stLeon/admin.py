from django.contrib import admin        # Exterior Library
from .models import Actualite, Anoter, Bienvenue, Batiments          # Project Models

admin.site.register(Actualite)
admin.site.register(Anoter)
admin.site.register(Bienvenue)
admin.site.register(Batiments)
