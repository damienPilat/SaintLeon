from django.urls import path    # Exterior Libraries
from . import views             # Local functions

app_name = 'stLeon'
urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('test_2', views.test_2, name="test_2")
]
