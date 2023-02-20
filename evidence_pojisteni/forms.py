from django.forms import ModelForm
from .models import Klient, Produkty

class KlientForm(ModelForm):
    class Meta:
        model = Klient
        fields = '__all__'

class ProduktForm(ModelForm):
    class Meta:
        model = Produkty
        fields = '__all__'
        

class ProduktFormUpgrade(ModelForm):
    class Meta:
        model = Produkty
        fields = '__all__'
        exclude = ['nazev_pojisteni', 'klient', 'predmet', 'platnost_od']