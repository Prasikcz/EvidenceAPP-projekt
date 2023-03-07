from django.forms import ModelForm
from .models import Klient, Produkty
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class KlientForm(ModelForm):
    class Meta:
        model = Klient
        fields = '__all__'
        exclude = ['user']

class ProduktForm(ModelForm):
    class Meta:
        model = Produkty
        fields = '__all__'

        

class ProduktFormUpgrade(ModelForm):
    class Meta:
        model = Produkty
        fields = '__all__'
        exclude = ['nazev_pojisteni', 'klient', 'predmet', 'platnost_od']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class KlientUserForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = ['rodne_cislo', 'ulice', 'cislo_popisne', 'mesto', 'psc', 'telefon']


        