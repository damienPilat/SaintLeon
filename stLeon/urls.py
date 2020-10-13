from django.urls import path    # Exterior Libraries
from . import views             # Local functions

app_name = 'stLeon'
urlpatterns = [
    path('', views.index, name='index'),
    path('batiments', views.batiments, name='batiments'),
    path('visite', views.visite_cult, name='visite'),
    path('test', views.test, name='test'),
    path('test_3', views.test_3, name='test_3')
]
