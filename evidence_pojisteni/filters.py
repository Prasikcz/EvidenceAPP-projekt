import django_filters
from .models import *
from django_filters import CharFilter

class KlientFilter(django_filters.FilterSet):
    #filtry použité na hlavní stránce, které slouží k vyhledání dat z databáze klientů
    rodne_cislo = CharFilter(field_name='rodne_cislo', lookup_expr='icontains')
    class Meta:
        model = Klient
        fields = '__all__'
        exclude = ['ulice', 'cislo_popisne', 'psc', 'mesto', 'date_created', 'e_mail', 'telefon']