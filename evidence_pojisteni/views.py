from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import KlientForm, ProduktForm, ProduktFormUpgrade, CreateUserForm
from .filters import KlientFilter

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Registrace uživatele {user} proběhla úspěšně')
            return redirect("login")


    context = {'form':form}
    return render(request, 'evidence_pojisteni/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Uživatelské jméno nebo heslo není správné')

        context = {}
        return render(request, 'evidence_pojisteni/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    #Způsob rendrování a filtrace dat na hlavní stránce
    klienti = Klient.objects.all().order_by("-id")
    produkty = Produkty.objects.all().order_by("-id")
    klientFilter = KlientFilter(request.GET, queryset=klienti)
    klienti = klientFilter.qs
    context = {'klienti':klienti, 'produkty':produkty, 'klientFilter':klientFilter}

    return render(request, 'evidence_pojisteni/index.html', context)


@login_required(login_url='login') 
def klient(request, pk):
    #Metoda sloučící v detailu klienta, podle níž se vypisují údaje o klientovi a jeho produktech
    klient = Klient.objects.get(pk=pk)
    produkty = klient.produkty_set.all()
    context = {'klient':klient, 'produkty':produkty}

    return render(request, 'evidence_pojisteni/klient.html', context)

@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def deleteProdukt(request, pk):
    #Metoda sloužící k vymazání klienta z db a navrácení na hlavní stránku
    produkt = Produkty.objects.get(pk=pk)
    context = {'produkt':produkt}
    if request.method == 'POST':
        produkt.delete() 
        messages.success(request, 'Produkt byl úspěšně smazán')
        return redirect("home")

    return render(request, 'evidence_pojisteni/delete_produkt.html', context)