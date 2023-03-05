from django.db import models
from django.contrib.auth.models import User
from .entry_conditions import *



class Klient(models.Model):

    #Třída reprezentující klienta pojišťovny
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    jmeno = models.CharField(max_length=200, null=True, verbose_name='Jméno')
    prijmeni = models.CharField(max_length=180, null=True, verbose_name='Příjmení')
    rodne_cislo = models.CharField(max_length=10, validators=[rodne_cislo], null=True, unique=True, verbose_name='Rodné číslo')
    ulice = models.CharField(max_length=180, null=True, verbose_name='Ulice')
    cislo_popisne = models.CharField(max_length=15, null=True, verbose_name='Číslo popisné')
    psc = models.CharField(max_length=5, validators=[psc], null=True, verbose_name='PSČ')
    mesto = models.CharField(max_length=120, null=True, verbose_name='Město')
    e_mail = models.EmailField(max_length=120, null=True, unique=True, verbose_name='E-mail')
    telefon = models.CharField(max_length=9,validators=[telefon], null=True, unique=True, verbose_name='Telefon')
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Datum registrace')


    def __str__(self):
        return  f"{self.jmeno} {self.prijmeni} RČ: {self.rodne_cislo}"

    class Meta:
            verbose_name="Klient"
            verbose_name_plural="Klienti"


class Produkty(models.Model):
    
    #Třída reprezentující nabízející produkty pojišťovny

    VYBER_PRODUKTU = (
    ('Pojištění majetku','Pojištění majetku'),
    ('Úrazové pojištění','Úrazové pojištění'),
    ('Cestovní pojištění','Cestovní pojištění'),
    )

    STATUS = (
        ('aktivní', 'Aktivní'),
        ('neaktivní', 'Neaktivní'),
    )

    DOBA_TRVANI = (
        ('1 rok', '1 rok'),
        ('2 roky', '2 roky'),
        ('Na neurčito', 'na neurčito'),
    )

    klient = models.ForeignKey(Klient, null=True, on_delete=models.SET_NULL)
    nazev_produktu = models.CharField(
        max_length=80,
        choices=VYBER_PRODUKTU,
        null=True,
        verbose_name='Název produktu')
    predmet = models.CharField(max_length=80, null=True, verbose_name='Předmět produktu')
    castka = models.CharField(max_length=10, validators=[only_int], null=True, verbose_name='Částka')
    doba_trvani = models.CharField(
        max_length=80,
        null=True,
        choices=DOBA_TRVANI,
        verbose_name='Doba trvání smlouvy',
        )
    platnost_od = models.CharField(max_length=20,null=True, verbose_name='Platnost od')
    platnost_do = models.CharField(max_length=20,null=True, verbose_name='Platnost do')
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Datum registrace')
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        null=True,
        default='aktivni',
        verbose_name='Status',
    )
    
    def __str__(self):
        return  f"{self.nazev_produktu} Doba trvání {self.doba_trvani}"

    class Meta:
            verbose_name="Produkt"
            verbose_name_plural="Produkty"

