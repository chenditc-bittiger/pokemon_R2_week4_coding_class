from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'pokemon', views.pokemons, name='pokemons'),
]
