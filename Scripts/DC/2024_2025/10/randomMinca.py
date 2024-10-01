# Hra "Divný Janko" bola úspešne naprogramovaná v Pythone. 
# Hra začína s Jankom v bode 50, a jeho cieľom je dostať sa do školy, 
# ktorá je v bode 100. Každé ráno sa posúva o 10 bodov smerom k škole, až kým nedosiahne bod 50. 
# Odtiaľ si začne hádzať mincou: ak padne znak, posunie sa o 10 bodov dopredu, a ak padne rub, posunie sa o 10 bodov dozadu. 
# Janko sa nemôže vrátiť domov, takže najnižší bod, na ktorý môže klesnúť, je 50. Hra pokračuje, až kým sa Janko nedostane do školy.
import random

def hod_minca():
    vysledok = random.choice([0,1])
    if vysledok == 0:
        return 10
    if vysledok == 1:
        return -10
 
aktualna_poloha = 50
domov = 0
skola = 100
dni = ["pondelok", 'utorok', 'streda', 'štvrtok', 'piatok']

for i in range(5):
    while aktualna_poloha != domov and aktualna_poloha != skola:
        vysledok = hod_minca()
        aktualna_poloha = aktualna_poloha + vysledok

    if aktualna_poloha == domov:
        print("Janko je doma v ", dni[i])
    if aktualna_poloha == skola:
        print("Janko je v škole v ", dni[i])

    aktualna_poloha = 50

