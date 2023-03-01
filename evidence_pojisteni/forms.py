from django.forms import ModelForm
from .models import Klient, Produkty
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


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

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']