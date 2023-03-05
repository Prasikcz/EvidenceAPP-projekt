from django.core.exceptions import ValidationError

# Sada metod, které snižují riziko, že budou do db zadány chybné údaje (tyto metody se vztahují na soubory v models.py)
def psc(value):
    #metoda, která zajišťuje, že budou zadány pouze celá čísla do PSČ
    if len(value) != 5 or value.isdigit()==False:
         raise ValidationError('Lze zadávat pouze čísla ve formátu [59101]')

    
def rodne_cislo(value): 
    #metoda, která zajišťuje, že budou zadány pouze celá čísla do RČ
    if value.isdigit()==False or len(value)<9:
        raise ValidationError('Lze zadávat pouze čísla ve formátu [5566771234]')

def only_int(value): 
    #metoda, která zajišťuje, že budou zadány pouze celá čísla do RČ
    if value.isdigit()==False:
        raise ValidationError('Lze zadat pouze kladné číslo') 


def telefon(value): 
    #metoda, která zajišťuje, že budou zadány pouze celá čísla do TEL.
    if value.isdigit()==False:
        raise ValidationError('Lze zadávat pouze čísla ve formátu [732205105]')
