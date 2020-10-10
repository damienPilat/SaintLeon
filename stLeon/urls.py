from django.urls import path    # Exterior Libraries
from . import views             # Local functions

app_name = 'stLeon'
urlpatterns = [
    path('', views.index, name='index'),
    path('batiments', views.batiments, name='batiments'),
    path('test', views.test, name='test')
]
