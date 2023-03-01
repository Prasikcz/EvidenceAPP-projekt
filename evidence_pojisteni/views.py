from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import KlientForm, ProduktForm, ProduktFormUpgrade, CreateUserForm
from .filters import KlientFilter
from django.contrib import messages
# Create your views here.

def registerPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'evidence_pojisteni/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'evidence_pojisteni/login.html', context)

def index(request):
    #Způsob rendrování a filtrace dat na hlavní stránce
    klienti = Klient.objects.all().order_by("-id")
    produkty = Produkty.objects.all().order_by("-id")
    klientFilter = KlientFilter(request.GET, queryset=klienti)
    klienti = klientFilter.qs
    context = {'klienti':klienti, 'produkty':produkty, 'klientFilter':klientFilter}

    return render(request, 'evidence_pojisteni/index.html', context)
    
def klient(request, pk):
    #Metoda sloučící v detailu klienta, podle níž se vypisují údaje o klientovi a jeho produktech
    klient = Klient.objects.get(pk=pk)
    produkty = klient.produkty_set.all()
    context = {'klient':klient, 'produkty':produkty}

    return render(request, 'evidence_pojisteni/klient.html', context)


def createKlient(request):
    #Metoda vyvolávající formulář k vytvoření klienta a jeho následné uložení do db
    form = KlientForm
    if request.method == 'POST':
        form = KlientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Klient byl úspěšně vytvořen')
            return redirect("home")

    context = {'form':form}
    return render(request, 'evidence_pojisteni/klient_form.html', context)

def updateKlient(request, pk):
    #Metoda sloužící k úpravě údajů klienta pomocí formuláře
    klient = Klient.objects.get(pk=pk)
    form = KlientForm(instance=klient)   

    if request.method == 'POST':
        form = KlientForm(request.POST, instance=klient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Klient byl úspěšně upraven')
            return redirect("klient", pk = klient.id)
    
    context = {'form':form, 'klient':klient}
    return render(request, 'evidence_pojisteni/update_klient.html', context)

def deleteKlient(request, pk):
    #Metoda sloužící k vymazání klienta z db a navrácení na hlavní stránku
    klient = Klient.objects.get(pk=pk)
    context = {'klient':klient}
    if request.method == 'POST':
        klient.delete()
        messages.success(request, 'Klient byl úspěšně smazán')
        return redirect("home")


    return render(request, 'evidence_pojisteni/delete_klient.html', context)

    
# produkt

def createProdukt(request, pk):
    #Metoda vyvolávající formulář k vytvoření produktu daného klienta a následného uložení do db
    klient = Klient.objects.get(pk=pk)

    form = ProduktForm(initial={'klient':klient})
    if request.method == 'POST':
        form = ProduktForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produkt byl úspěšně vytvořen')
            return redirect("klient", pk = klient.id)

    context = {'form':form, 'klient':klient}
    return render(request, 'evidence_pojisteni/produkt_form.html', context)

def produkt(request, pk):
    #Metoda sloučící k rendrování detailu produktu klienta
    produkt = Produkty.objects.get(pk=pk)
    context = {'produkty':produkt}

    return render(request, 'evidence_pojisteni/produkt.html', context)


def updateProdukt(request, pk):
    #Metoda sloužící k úpravě údajů klienta pomocí formuláře
    produkt = Produkty.objects.get(pk=pk)
    form = ProduktFormUpgrade(instance=produkt) 

    if request.method == 'POST':
        form = ProduktFormUpgrade(request.POST, instance=produkt)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produkt byl úspěšně upraven')
            
            return redirect("produkt", pk = produkt.id)
    
    context = {'form':form, 'produkt':produkt, 'klient':klient}
    return render(request, 'evidence_pojisteni/update_produkt.html', context)


def deleteProdukt(request, pk):
    #Metoda sloužící k vymazání klienta z db a navrácení na hlavní stránku
    produkt = Produkty.objects.get(pk=pk)
    context = {'produkt':produkt}
    if request.method == 'POST':
        produkt.delete() 
        messages.success(request, 'Produkt byl úspěšně smazán')
        return redirect("home")

    return render(request, 'evidence_pojisteni/delete_produkt.html', context)